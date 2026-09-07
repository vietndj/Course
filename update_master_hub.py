# -*- coding: utf-8 -*-
import os
from build_12_baitap import EXERCISES

def build_master_hub():
    master_path = '/Users/vietmac/Documents/CODE/course/lopmarketingbaitap.html'
    
    # Category mapping
    def get_category(ex_id):
        if ex_id in ["01", "02", "07"]:
            return "pressure" # Áp lực & Bế tắc
        elif ex_id in ["04", "10"]:
            return "insight" # Giác ngộ & Thức tỉnh
        elif ex_id in ["03", "06", "09", "11"]:
            return "action" # Thực chiến & Thử nghiệm
        else:
            return "calm" # Thành quả & Lắng đọng

    # Build Overview Cards HTML
    cards_html_list = []
    detail_sections_list = []
    
    for ex in EXERCISES:
        ex_id = ex["id"]
        cat = get_category(ex_id)
        
        # Overview Card
        c_html = f"""
        <div class="overview-card" data-category="{cat}" onclick="showExercise('{ex_id}')" id="card-tab-{ex_id}">
          <div class="overview-img-box">
            <img src="{ex['avatar']}" alt="{ex['title']}" loading="lazy">
            <span class="card-badge-top" style="background:#1a73e8; color:#fff;">Bài tập {ex_id}</span>
            <span class="card-outfit-tag">{ex['outfit']}</span>
          </div>
          <div class="overview-body">
            <div class="overview-card-title">{ex['title']}</div>
            <div class="overview-quote">"{ex['voice'][:75]}..."</div>
            <div class="overview-t25"><b>Tâm lý:</b> {ex['state']}</div>
            <div style="display:flex; gap:8px; margin-top:auto;">
              <a href="{ex['slug']}" target="_blank" class="overview-btn" style="flex:1;">Mở Trang Riêng ↗</a>
              <button type="button" class="overview-btn" style="background:#0284c7; color:#fff; border:none;" onclick="event.stopPropagation(); showExercise('{ex_id}')">Xem 5 Shot ↓</button>
            </div>
          </div>
        </div>"""
        cards_html_list.append(c_html)
        
        # Detailed Exercise Section
        beats_list = []
        for idx, (b_title, b_time, b_size, b_angle, b_dir, b_voice, b_tip) in enumerate(ex["shots"], 1):
            img_path = f"{ex['frame_dir']}/shot{idx}.jpg"
            b_html = f"""
          <div class="beat-card">
            <div class="beat-img-container" onclick="openLightbox('{img_path}', 'Shot {idx} • {b_title}', '{b_time}', '{b_voice}', '{b_tip}')">
              <img src="{img_path}" alt="{b_title}" loading="lazy">
              <span class="beat-badge-top badge-action">{b_size}</span>
              <span class="beat-time-tag">{b_time}</span>
            </div>
            <div class="beat-content">
              <div class="beat-id-title">{idx}. {b_title}</div>
              <div class="beat-voice-pill">🎙️ "{b_voice}"</div>
              <table class="specs-table">
                <tr><td class="spec-name">Cỡ cảnh:</td><td>{b_size}</td></tr>
                <tr><td class="spec-name">Góc máy:</td><td>{b_angle}</td></tr>
                <tr><td class="spec-name">Hướng:</td><td>{b_dir}</td></tr>
              </table>
              <div style="font-size:11px; color:#94a3b8; margin-top:auto; padding-top:6px; border-top:1px dashed rgba(255,255,255,0.08);">
                💡 {b_tip}
              </div>
            </div>
          </div>"""
            beats_list.append(b_html)
        beats_joined = "\n".join(beats_list)
        
        # Reshoot list
        reshoot_items = []
        for r_title, r_desc in ex["reshoots"]:
            reshoot_items.append(f'<li style="margin-bottom:8px;"><b>{r_title}:</b> {r_desc}</li>')
        reshoots_joined = "\n".join(reshoot_items)

        d_html = f"""
      <!-- EXERCISE {ex_id} DETAIL -->
      <div class="exercise-detail-wrap" id="detail-bt{ex_id}">
        <div class="master-audio-box">
          <div class="master-audio-content">
            <div class="master-voice-icon">🎙️</div>
            <div>
              <div class="master-voice-title">Bài tập {ex_id} • Lời thoại Voice-Over ngầm</div>
              <div class="master-voice-text" id="voice-text-{ex_id}">"{ex['voice']}"</div>
            </div>
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <button class="copy-btn" onclick="copyVoice('{ex_id}')">Sao chép kịch bản</button>
            <a href="{ex['slug']}" target="_blank" class="copy-btn" style="background:#0284c7; border-color:#0284c7; text-decoration:none;">Mở trang riêng ↗</a>
          </div>
        </div>

        <!-- 4 Tiers of Truth -->
        <div class="tiers-section">
          <div class="tiers-header">
            <div class="tiers-title">
              <span>🧠 BẢN ĐỒ TÂM LÝ HỌC (BÀI TẬP {ex_id})</span>
              <span class="tag tag-cyan">{ex['state']}</span>
            </div>
            <span style="font-size:12px; color:var(--text-muted);">Trang phục: {ex['outfit']}</span>
          </div>
          <div class="tiers-grid-4">
            <div class="tier-card t1">
              <div class="tier-card-head">Tầng 1 • Nói đãi bôi</div>
              <div class="tier-card-content">"{ex['t1']}"</div>
              <div class="tier-sub">Lý do bề nổi: cái cớ an toàn ai cũng nói được.</div>
            </div>
            <div class="tier-card t2">
              <div class="tier-card-head">Tầng 2 • Cảm giác thật</div>
              <div class="tier-card-content">"{ex['t2']}"</div>
              <div class="tier-sub">Hành vi thật: thao tác lúng túng đời thường.</div>
            </div>
            <div class="tier-card t25">
              <div class="tier-card-head">Tầng 2.5 • Thể diện người lớn</div>
              <div class="tier-card-content">"{ex['t25']}"</div>
              <div class="tier-sub">Điểm nghẽn thể diện: sợ người ngoài chê cười, làm màu.</div>
            </div>
            <div class="tier-card t3">
              <div class="tier-card-head">Tầng 3 • Tim đen ngượng miệng</div>
              <div class="tier-card-content">"{ex['t3']}"</div>
              <div class="tier-sub">Sự thật giấu kín: nỗi sợ và điểm nghẽn thực sự.</div>
            </div>
          </div>
        </div>

        <!-- 5 Beats Grid -->
        <div style="margin-bottom:14px; display:flex; justify-content:space-between; align-items:center;">
          <h3 style="font-size:16px; font-weight:800; color:#fff;">🎬 CHI TIẾT 5 CÚ MÁY BĂM NHỎ (BÀI TẬP {ex_id})</h3>
          <span style="font-size:12px; color:var(--cyan);">Bấm vào ảnh để phóng to chi tiết</span>
        </div>
        <div class="storyboard-grid-5">
          {beats_joined}
        </div>

        <!-- Reshoot Box -->
        <div style="background:#090e17; border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px 22px; margin-top:20px;">
          <h4 style="font-size:14px; font-weight:800; color:#fde047; margin-bottom:10px;">📍 3 Gợi Ý Bối Cảnh Quay Lại Ngoài Lớp Học:</h4>
          <ul style="padding-left:20px; font-size:13px; color:#cbd5e1; line-height:1.6;">
            {reshoots_joined}
          </ul>
        </div>
      </div>"""
        detail_sections_list.append(d_html)
        
    cards_html = "\n".join(cards_html_list)
    details_html = "\n".join(detail_sections_list)
    
    # Master HTML
    master_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kho 12 Bài Tập Thực Chiến • Băm Cảnh Trám Marketing | Mentor Nguyễn Đức Việt</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #060911;
      --bg-surface: #0c121e;
      --bg-card: #121a2b;
      --bg-card-hover: #18233a;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(56, 189, 248, 0.35);
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --cyan: #38bdf8;
      --cyan-glow: rgba(56, 189, 248, 0.15);
      --amber: #f59e0b;
      --amber-glow: rgba(245, 158, 11, 0.15);
      --emerald: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.15);
      --purple: #a855f7;
      --purple-glow: rgba(168, 85, 247, 0.15);
      --rose: #f43f5e;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-primary);
      line-height: 1.6;
      padding-bottom: 80px;
    }}
    
    .top-header {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(6, 9, 17, 0.94);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 24px;
      display: flex; justify-content: space-between; align-items: center; gap: 16px;
    }}
    .brand-group {{ display: flex; align-items: center; gap: 12px; }}
    .brand-badge {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #fff; font-size: 11px; font-weight: 800; padding: 5px 12px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.5px;
    }}
    .header-title {{ font-size: 14.5px; font-weight: 700; color: var(--text-primary); }}
    .header-controls {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    .nav-pill {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); color: var(--text-secondary);
      font-size: 12px; font-weight: 600; padding: 6px 12px; border-radius: var(--radius-sm); text-decoration: none; cursor: pointer; transition: all 0.2s;
    }}
    .nav-pill:hover, .nav-pill.active {{ background: var(--cyan); color: #000; font-weight: 700; border-color: var(--cyan); }}

    .container {{ max-width: 1400px; margin: 0 auto; padding: 24px 20px; }}

    /* Hero Banner */
    .hero {{
      background: linear-gradient(180deg, #101827 0%, #090e17 100%);
      border: 1px solid rgba(56, 189, 248, 0.22); border-radius: var(--radius-lg); padding: 28px 32px; margin-bottom: 30px;
    }}
    .hero-tags {{ display: flex; gap: 8px; margin-bottom: 14px; flex-wrap: wrap; }}
    .tag {{ font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 6px; display: inline-flex; align-items: center; gap: 5px; }}
    .tag-cyan {{ background: var(--cyan-glow); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .tag-amber {{ background: var(--amber-glow); color: var(--amber); border: 1px solid rgba(245, 158, 11, 0.3); }}
    .tag-emerald {{ background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3); }}
    
    .hero h1 {{ font-size: 26px; font-weight: 800; margin-bottom: 12px; color: #fff; line-height: 1.35; }}
    .hero-lead {{ font-size: 14.5px; color: #cbd5e1; line-height: 1.7; max-width: 1050px; margin-bottom: 20px; }}
    .hero-lead b {{ color: var(--cyan); }}

    .metrics-bar {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;
      background: rgba(0, 0, 0, 0.4); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 14px 18px;
    }}
    .metric-label {{ font-size: 10.5px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; margin-bottom: 2px; }}
    .metric-value {{ font-size: 16px; font-weight: 800; color: var(--text-primary); }}

    /* Emotion Filter Bar */
    .filter-bar {{
      display: flex; gap: 8px; margin-bottom: 24px; flex-wrap: wrap; align-items: center;
    }}
    .filter-btn {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); color: var(--text-secondary);
      font-size: 12.5px; font-weight: 700; padding: 7px 16px; border-radius: 100px; cursor: pointer; transition: all 0.2s;
    }}
    .filter-btn:hover, .filter-btn.active {{
      background: var(--cyan); color: #000; border-color: var(--cyan);
    }}

    /* Exercise Overview Grid */
    .overview-grid {{
      display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-bottom: 36px;
    }}
    @media (max-width: 1200px) {{ .overview-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
    @media (max-width: 850px) {{ .overview-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 550px) {{ .overview-grid {{ grid-template-columns: 1fr; }} }}

    .overview-card {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
      overflow: hidden; display: flex; flex-direction: column; cursor: pointer; transition: all 0.25s ease;
      position: relative;
    }}
    .overview-card:hover {{ transform: translateY(-4px); border-color: var(--cyan); box-shadow: 0 12px 30px rgba(0,0,0,0.5); }}
    .overview-card.active-tab {{ border-color: var(--cyan); box-shadow: 0 0 20px rgba(56, 189, 248, 0.25); }}

    .overview-img-box {{
      width: 100%; aspect-ratio: 9 / 16; overflow: hidden; position: relative; background: #000; max-height: 280px;
    }}
    .overview-img-box img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease; }}
    .overview-card:hover .overview-img-box img {{ transform: scale(1.05); }}

    .card-badge-top {{
      position: absolute; top: 10px; left: 10px; z-index: 2; font-size: 10px; font-weight: 800;
      padding: 4px 9px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.5px;
    }}
    .card-outfit-tag {{
      position: absolute; bottom: 8px; right: 8px; z-index: 2;
      background: rgba(0, 0, 0, 0.85); border: 1px solid rgba(255,255,255,0.15);
      font-size: 10px; font-weight: 700; color: #f8fafc; padding: 3px 8px; border-radius: 4px;
    }}

    .overview-body {{ padding: 16px; display: flex; flex-direction: column; gap: 10px; flex: 1; }}
    .overview-card-title {{ font-size: 14px; font-weight: 800; color: var(--text-primary); line-height: 1.35; }}
    .overview-quote {{
      font-size: 12px; color: #fde047; font-style: italic; background: rgba(253, 224, 71, 0.06);
      padding: 8px 10px; border-radius: 6px; border-left: 3px solid #fde047; line-height: 1.5;
    }}
    .overview-t25 {{ font-size: 11.5px; color: var(--text-secondary); line-height: 1.5; }}
    .overview-btn {{
      background: rgba(56, 189, 248, 0.12); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3);
      font-size: 11px; font-weight: 700; padding: 6px 10px; border-radius: 6px; text-align: center; text-decoration: none; transition: 0.2s; cursor: pointer;
    }}
    .overview-btn:hover {{ background: var(--cyan); color: #000; }}

    /* Detailed Exercise Section */
    .exercise-detail-wrap {{ display: none; margin-bottom: 40px; }}
    .exercise-detail-wrap.active {{ display: block; animation: fadeIn 0.3s ease; }}
    @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: translateY(0); }} }}

    /* Master Audio / Voiceover Box */
    .master-audio-box {{
      background: linear-gradient(90deg, rgba(56, 189, 248, 0.1) 0%, rgba(20, 31, 51, 0.7) 100%);
      border: 1px solid rgba(56, 189, 248, 0.3); border-radius: var(--radius-lg); padding: 20px 26px; margin-bottom: 24px;
      display: flex; align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap;
    }}
    .master-audio-content {{ display: flex; align-items: center; gap: 16px; flex: 1; min-width: 280px; }}
    .master-voice-icon {{
      font-size: 22px; background: var(--cyan-glow); color: var(--cyan); width: 48px; height: 48px;
      border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; border: 1px solid var(--cyan);
    }}
    .master-voice-title {{ font-size: 11px; color: var(--cyan); font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }}
    .master-voice-text {{ font-size: 15px; font-weight: 700; color: #fde047; font-style: italic; line-height: 1.6; }}
    .copy-btn {{
      background: #1a2538; color: #f8fafc; border: 1px solid var(--cyan); padding: 8px 16px;
      border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 6px; transition: all 0.2s;
    }}
    .copy-btn:hover {{ background: var(--cyan); color: #000; }}

    /* 4 Tiers of Truth Section */
    .tiers-section {{
      background: linear-gradient(180deg, #101929 0%, #0a0f19 100%);
      border: 1px solid rgba(56, 189, 248, 0.22); border-radius: var(--radius-lg); padding: 22px 26px; margin-bottom: 24px;
    }}
    .tiers-header {{
      display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;
      margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .tiers-title {{ font-size: 14.5px; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 8px; }}
    .tiers-grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }}
    @media (max-width: 1180px) {{ .tiers-grid-4 {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 650px) {{ .tiers-grid-4 {{ grid-template-columns: 1fr; }} }}
    
    .tier-card {{
      background: #080d16; border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 16px 14px;
      display: flex; flex-direction: column; gap: 8px;
    }}
    .tier-card.t1 {{ border-left: 4px solid #ef4444; }}
    .tier-card.t2 {{ border-left: 4px solid #f59e0b; }}
    .tier-card.t25 {{ border-left: 4px solid #a855f7; background: linear-gradient(180deg, rgba(168, 85, 247, 0.08) 0%, #080d16 100%); }}
    .tier-card.t3 {{ border-left: 4px solid #10b981; }}

    .tier-card-head {{ font-size: 10.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; }}
    .tier-card.t1 .tier-card-head {{ color: #f87171; }}
    .tier-card.t2 .tier-card-head {{ color: #fbbf24; }}
    .tier-card.t25 .tier-card-head {{ color: #c084fc; }}
    .tier-card.t3 .tier-card-head {{ color: #34d399; }}
    
    .tier-card-content {{ font-size: 12.5px; color: #f1f5f9; line-height: 1.6; flex: 1; }}
    .tier-sub {{
      font-size: 11px; color: var(--text-muted); line-height: 1.45; border-top: 1px dashed rgba(255,255,255,0.08); padding-top: 6px; margin-top: 4px;
    }}

    /* 5-Beats Storyboard Grid */
    .storyboard-grid-5 {{
      display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; margin-bottom: 24px;
    }}
    @media (max-width: 1280px) {{ .storyboard-grid-5 {{ grid-template-columns: repeat(3, 1fr); }} }}
    @media (max-width: 850px) {{ .storyboard-grid-5 {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 540px) {{ .storyboard-grid-5 {{ grid-template-columns: 1fr; }} }}

    .beat-card {{
      background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
      overflow: hidden; display: flex; flex-direction: column; transition: transform 0.2s, border-color 0.2s;
    }}
    .beat-card:hover {{ border-color: var(--border-accent); transform: translateY(-2px); }}

    .beat-img-container {{
      position: relative; width: 100%; aspect-ratio: 9 / 16; background: #000; overflow: hidden; cursor: pointer;
    }}
    .beat-img-container img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease; }}
    .beat-img-container:hover img {{ transform: scale(1.04); }}

    .beat-badge-top {{
      position: absolute; top: 8px; left: 8px; z-index: 2; font-size: 9px; font-weight: 800;
      padding: 3px 8px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.5px;
    }}
    .badge-action {{ background: rgba(56, 189, 248, 0.9); color: #000; }}

    .beat-time-tag {{
      position: absolute; top: 8px; right: 8px; z-index: 2; background: rgba(0, 0, 0, 0.85);
      border: 1px solid rgba(255,255,255,0.15); color: var(--cyan); font-family: 'JetBrains Mono', monospace;
      font-size: 9.5px; font-weight: 700; padding: 2px 6px; border-radius: 4px;
    }}

    .beat-content {{ padding: 12px; display: flex; flex-direction: column; gap: 8px; flex: 1; }}
    .beat-id-title {{ font-size: 13px; font-weight: 800; color: var(--text-primary); line-height: 1.3; }}
    .beat-voice-pill {{
      background: rgba(253, 224, 71, 0.08); border-left: 3px solid #fde047; padding: 5px 8px;
      border-radius: 0 4px 4px 0; font-size: 11px; font-weight: 600; color: #fef08a; line-height: 1.45;
    }}

    .specs-table {{
      width: 100%; font-size: 10.5px; border-collapse: collapse; background: rgba(0, 0, 0, 0.28);
      border-radius: 6px; overflow: hidden; margin-top: 2px;
    }}
    .specs-table tr {{ border-bottom: 1px solid rgba(255, 255, 255, 0.04); }}
    .specs-table tr:last-child {{ border-bottom: none; }}
    .specs-table td {{ padding: 4px 7px; }}
    .specs-table td.spec-name {{ color: var(--text-muted); font-weight: 600; width: 40%; }}

    /* Lightbox Modal */
    .lightbox-overlay {{
      position: fixed; inset: 0; z-index: 1000; background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(12px);
      display: none; align-items: center; justify-content: center; padding: 20px;
    }}
    .lightbox-overlay.active {{ display: flex; }}
    .lightbox-card {{
      background: var(--bg-surface); border: 1px solid var(--border-accent); border-radius: var(--radius-lg);
      max-width: 880px; width: 100%; max-height: 90vh; overflow: hidden; display: flex; flex-direction: row;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    }}
    @media (max-width: 768px) {{ .lightbox-card {{ flex-direction: column; max-height: 85vh; overflow-y: auto; }} }}
    .lightbox-media {{ flex: 1.1; background: #000; position: relative; aspect-ratio: 9/16; max-height: 80vh; }}
    .lightbox-media img {{ width: 100%; height: 100%; object-fit: cover; }}
    .lightbox-sidebar {{ flex: 1; padding: 24px; display: flex; flex-direction: column; gap: 14px; overflow-y: auto; }}
    .lightbox-close-btn {{
      align-self: flex-end; background: rgba(255,255,255,0.1); border: none; color: #fff;
      width: 32px; height: 32px; border-radius: 50%; cursor: pointer; font-size: 16px;
    }}

    .toast {{
      position: fixed; bottom: 24px; right: 24px; z-index: 1000; background: var(--emerald); color: #fff;
      font-weight: 700; font-size: 13px; padding: 10px 18px; border-radius: 8px; display: none;
    }}
    .toast.show {{ display: block; }}
  </style>
</head>
<body>

  <header class="top-header">
    <div class="brand-group">
      <span class="brand-badge">FEDU MASTER HUB</span>
      <span class="header-title">Kho 12 Bài Tập Băm Cảnh Trám Marketing</span>
    </div>
    <div class="header-controls">
      <a href="index.html" class="nav-pill">← Về Kho Khóa Học</a>
    </div>
  </header>

  <div class="container">
    
    <!-- Hero Banner -->
    <div class="hero">
      <div class="hero-tags">
        <span class="tag tag-cyan">MARKETING PT</span>
        <span class="tag tag-amber">12 BÀI TẬP BĂM CẢNH</span>
        <span class="tag tag-emerald">12 PHONG CÁCH TRANG PHỤC</span>
      </div>
      <h1>KHO BÀI TẬP THỰC HÀNH QUAY CẢNH TRÁM TẠI LỚP (B-ROLL)</h1>
      <p class="hero-lead">
        Nguyên tắc sống còn: <b>Không bao giờ để khung hình chết dí một chỗ</b>. 
        Mỗi bài tập dưới đây hướng dẫn học viên băm nhỏ 1 hành động bình thường thành 5 cỡ cảnh khác nhau (MCU, CU, Macro, POV/OTS, Low angle) ngay tại bàn học, 
        tải trọn vẹn từng trạng thái tâm lý trong video voice-over. Sau khi thành thạo, học viên có thể mang về quay lại ở các bối cảnh đời thực tương đương.
      </p>
      <div class="metrics-bar">
        <div>
          <div class="metric-label">Tổng số bài tập</div>
          <div class="metric-value">12 Bài tập thực chiến</div>
        </div>
        <div>
          <div class="metric-label">Tổng số cỡ cảnh</div>
          <div class="metric-value">60 Cú máy băm nhỏ</div>
        </div>
        <div>
          <div class="metric-label">Trang phục anh Việt</div>
          <div class="metric-value">12 Phong cách khác nhau</div>
        </div>
        <div>
          <div class="metric-label">Trục thay đổi</div>
          <div class="metric-value">Cỡ cảnh • Góc máy • Hướng</div>
        </div>
      </div>
    </div>

    <!-- Emotion Filter Bar -->
    <div class="filter-bar">
      <span style="font-size:12px; font-weight:700; color:var(--text-muted); margin-right:4px;">LỌC TÂM LÝ:</span>
      <button class="filter-btn active" onclick="filterCards('all')">Tất cả (12)</button>
      <button class="filter-btn" onclick="filterCards('pressure')">Áp lực & Bế tắc (3)</button>
      <button class="filter-btn" onclick="filterCards('insight')">Giác ngộ & Thức tỉnh (2)</button>
      <button class="filter-btn" onclick="filterCards('action')">Thực chiến & Thử nghiệm (4)</button>
      <button class="filter-btn" onclick="filterCards('calm')">Thành quả & Lắng đọng (3)</button>
    </div>

    <!-- Overview Grid -->
    <div class="overview-grid" id="master-grid">
      {cards_html}
    </div>

    <!-- Detail Sections Container -->
    <div id="details-container">
      {details_html}
    </div>

  </div>

  <!-- Lightbox Modal -->
  <div class="lightbox-overlay" id="lightbox" onclick="closeLightbox(event)">
    <div class="lightbox-card" onclick="event.stopPropagation()">
      <div class="lightbox-media">
        <img id="lb-img" src="" alt="Frame Detail">
      </div>
      <div class="lightbox-sidebar">
        <button class="lightbox-close-btn" onclick="closeLightbox()">✕</button>
        <span class="tag tag-cyan" id="lb-time">00:00</span>
        <h3 id="lb-title" style="font-size:16px; font-weight:800; color:#fff;">Tiêu đề</h3>
        <div class="beat-voice-pill" id="lb-voice" style="font-size:13px;">Lời thoại</div>
        <div style="font-size:12.5px; color:#94a3b8; line-height:1.6; border-top:1px dashed rgba(255,255,255,0.1); padding-top:10px;" id="lb-tip">Mẹo đạo diễn</div>
      </div>
    </div>
  </div>

  <div class="toast" id="toast-msg">Đã sao chép kịch bản voice-over!</div>

  <script>
    let currentActiveBt = "01";

    function showExercise(id) {{
      // Update tabs
      document.querySelectorAll('.overview-card').forEach(c => c.classList.remove('active-tab'));
      const activeCard = document.getElementById('card-tab-' + id);
      if (activeCard) activeCard.classList.add('active-tab');

      // Update detail sections
      document.querySelectorAll('.exercise-detail-wrap').forEach(d => d.classList.remove('active'));
      const activeDetail = document.getElementById('detail-bt' + id);
      if (activeDetail) {{
        activeDetail.classList.add('active');
        activeDetail.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}
      currentActiveBt = id;
    }}

    function filterCards(cat) {{
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');

      document.querySelectorAll('.overview-card').forEach(card => {{
        if (cat === 'all' || card.dataset.category === cat) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    function copyVoice(id) {{
      const el = document.getElementById('voice-text-' + id);
      if (!el) return;
      const text = el.innerText.replace(/^"|"$/g, '').trim();
      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById('toast-msg');
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2200);
      }});
    }}

    function openLightbox(imgSrc, title, time, voice, tip) {{
      document.getElementById('lb-img').src = imgSrc;
      document.getElementById('lb-title').innerText = title;
      document.getElementById('lb-time').innerText = time;
      document.getElementById('lb-voice').innerText = '🎙️ ' + voice;
      document.getElementById('lb-tip').innerHTML = '💡 <b>Mẹo Ông Giáo:</b> ' + tip;
      document.getElementById('lightbox').classList.add('active');
    }}

    function closeLightbox() {{
      document.getElementById('lightbox').classList.remove('active');
    }}

    // Default activate BT01
    document.addEventListener('DOMContentLoaded', () => {{
      showExercise('01');
    }});
  </script>
</body>
</html>
"""

    with open(master_path, 'w', encoding='utf-8') as f:
        f.write(master_html)
    print("Master hub lopmarketingbaitap.html updated successfully with all 12 exercises!")

if __name__ == '__main__':
    build_master_hub()
