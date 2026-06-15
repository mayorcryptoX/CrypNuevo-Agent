import cv2, sys, os, math
from PIL import Image, ImageDraw, ImageFont

def extract(vid_path, out_dir, n_target=20, cols=4, cell_w=560):
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(vid_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    dur = total / fps if fps else 0
    if dur <= 0:
        print("bad video", vid_path); return []
    # sample evenly, skip first/last 3% (intro/outro)
    start, end = dur*0.02, dur*0.98
    times = [start + (end-start)*i/(n_target-1) for i in range(n_target)]
    saved = []
    for t in times:
        cap.set(cv2.CAP_PROP_POS_MSEC, t*1000)
        ok, frame = cap.read()
        if not ok: continue
        # skip near-black frames (intro)
        if frame.mean() < 12: continue
        ts = f"{int(t//60):02d}{int(t%60):02d}"
        fn = os.path.join(out_dir, f"frame-{ts}.jpg")
        cv2.imwrite(fn, frame, [cv2.IMWRITE_JPEG_QUALITY, 88])
        saved.append((t, fn))
    cap.release()
    if not saved: return []
    # build contact sheet
    rows = math.ceil(len(saved)/cols)
    sample = Image.open(saved[0][1]); ar = sample.height/sample.width
    cw, ch = cell_w, int(cell_w*ar); pad=4; lbl=18
    sheet = Image.new("RGB", (cols*cw+(cols+1)*pad, rows*(ch+lbl)+(rows+1)*pad), (10,10,10))
    d = ImageDraw.Draw(sheet)
    try: font = ImageFont.truetype("arial.ttf", 14)
    except: font = ImageFont.load_default()
    for i,(t,fn) in enumerate(saved):
        r,c = divmod(i, cols)
        x = pad + c*(cw+pad); y = pad + r*(ch+lbl+pad)
        im = Image.open(fn).resize((cw,ch))
        sheet.paste(im, (x, y+lbl))
        d.text((x+2,y), f"{int(t//60):02d}:{int(t%60):02d}", fill=(255,220,0), font=font)
    cs_path = out_dir + "-contact-sheet.jpg"
    sheet.save(cs_path, quality=85)
    print(f"{os.path.basename(vid_path)}: {len(saved)} frames, dur {int(dur//60)}m{int(dur%60)}s, sheet {sheet.size} -> {cs_path}")
    return saved

if __name__ == "__main__":
    extract(sys.argv[1], sys.argv[2])
