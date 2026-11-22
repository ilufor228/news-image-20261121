#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont

def draw_newspaper():
    width, height = 1024, 1024
    img = Image.new("RGB", (width, height), color="#fcfbf7")
    draw = ImageDraw.Draw(img)

    # Fonts
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_regular_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    
    font_masthead = ImageFont.truetype(font_path, 44)
    font_subhead = ImageFont.truetype(font_path, 15)
    font_panel_title = ImageFont.truetype(font_path, 14)
    font_panel_text = ImageFont.truetype(font_path, 11)

    # Header section
    draw.rectangle([20, 20, 1004, 125], fill="#111111")
    draw.text((36, 30), "THE GLOBAL CHRONICLE", fill="#ffffff", font=font_masthead)
    draw.text((36, 84), "SATURDAY, 21 NOVEMBER 2026  |  WORLD EDITION", fill="#e0e0e0", font=font_subhead)
    draw.text((730, 84), "PRICE: $2.50", fill="#e0e0e0", font=font_subhead)

    # Thin separator line
    draw.rectangle([20, 135, 1004, 138], fill="#111111")

    # Panels configuration (3 rows, 2 columns)
    # Box height: ~275 each. Total height from 145 to 995.
    panels = [
        {
            "box": (20, 145, 502, 420),
            "title": "IRAN STRIKES US SITES IN BAHRAIN",
            "desc": "Missile strikes hit US radar in Bahrain; F-16 damaged as Middle East tensions surge.",
            "type": "iran"
        },
        {
            "box": (522, 145, 1004, 420),
            "title": "COP31 DEADLOCK IN ANTALYA",
            "desc": "Climate summit in Antalya overruns deadline amid deadlock over fossil fuel phaseout.",
            "type": "cop31"
        },
        {
            "box": (20, 432, 502, 707),
            "title": "FBI DATABASE HACKED",
            "desc": "FBI probes massive breach into US national criminal database used by police nationwide.",
            "type": "fbi"
        },
        {
            "box": (522, 432, 1004, 707),
            "title": "PERU EARTHQUAKE 6.7",
            "desc": "Magnitude 6.7 earthquake strikes central Peru, sending panicked crowds fleeing cinemas.",
            "type": "peru"
        },
        {
            "box": (20, 719, 502, 994),
            "title": "GTA VI SMASHES RECORDS",
            "desc": "Grand Theft Auto VI launches to unprecedented numbers, breaking all entertainment records.",
            "type": "gta"
        },
        {
            "box": (522, 719, 1004, 994),
            "title": "WALL STREET SLIDES",
            "desc": "US stocks plunge in AI stock sell-off; S&P 500 and Dow Jones enter deep correction.",
            "type": "wallstreet"
        }
    ]

    for p in panels:
        bx1, by1, bx2, by2 = p["box"]
        # Panel container box
        draw.rectangle([bx1, by1, bx2, by2], outline="#333333", width=2, fill="#ffffff")
        # Panel title banner
        draw.rectangle([bx1, by1, bx2, by1 + 30], fill="#222222")
        draw.text((bx1 + 10, by1 + 7), p["title"], fill="#ffffff", font=font_panel_title)

        # Drawing area inside panel
        dw1, dy1, dw2, dy2 = bx1 + 12, by1 + 38, bx2 - 12, by2 - 40
        
        # Draw custom illustrations based on panel type
        if p["type"] == "iran":
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#f5f5f5")
            # US Base label placed cleanly at top left
            draw.text((dw1 + 15, dy1 + 10), "US BASE & RADAR", fill="#333", font=font_panel_title)
            # Base building box
            draw.rectangle([dw1 + 15, dy1 + 35, dw1 + 115, dy1 + 75], fill="#444")
            # Radar dish clear of text
            draw.arc([dw1 + 140, dy1 + 30, dw1 + 200, dy1 + 90], start=180, end=360, fill="#222", width=3)
            draw.line([dw1 + 170, dy1 + 60, dw1 + 170, dy1 + 90], fill="#222", width=3)
            # Missile arc & explosion
            draw.line([dw2 - 20, dy1 + 15, dw1 + 90, dy1 + 50], fill="#cc0000", width=4)
            draw.ellipse([dw1 + 75, dy1 + 35, dw1 + 105, dy1 + 65], fill="#ff6600")
            draw.text((dw2 - 110, dy1 + 15), "F-16 HIT", fill="#cc0000", font=font_panel_title)

        elif p["type"] == "cop31":
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#eef2f5")
            draw.rectangle([dw1 + 15, dy1 + 10, dw1 + 220, dy1 + 35], fill="#1b4332")
            draw.text((dw1 + 22, dy1 + 14), "COP31 ANTALYA", fill="#ffffff", font=font_panel_title)
            # Scales of deadlock
            draw.line([dw1 + 115, dy1 + 45, dw1 + 115, dy1 + 95], fill="#333", width=3)
            draw.line([dw1 + 65, dy1 + 55, dw1 + 165, dy1 + 55], fill="#333", width=3)
            draw.rectangle([dw1 + 50, dy1 + 55, dw1 + 80, dy1 + 75], fill="#d90429")
            draw.rectangle([dw1 + 150, dy1 + 55, dw1 + 180, dy1 + 75], fill="#2b9348")
            draw.text((dw1 + 185, dy1 + 60), "DEADLOCK", fill="#d90429", font=font_panel_title)

        elif p["type"] == "fbi":
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#111827")
            draw.rectangle([dw1 + 15, dy1 + 10, dw1 + 190, dy1 + 85], outline="#ef4444", width=3, fill="#1f2937")
            draw.text((dw1 + 25, dy1 + 18), "FBI DATABASE", fill="#9ca3af", font=font_panel_title)
            draw.text((dw1 + 25, dy1 + 38), "BREACHED!", fill="#ef4444", font=font_panel_title)
            # Binary stream
            draw.text((dw1 + 205, dy1 + 18), "010068 1101", fill="#10b981", font=font_panel_text)
            draw.text((dw1 + 205, dy1 + 38), "SQL INJECTION", fill="#ef4444", font=font_panel_text)
            draw.text((dw1 + 205, dy1 + 58), "SEC_FAIL", fill="#f59e0b", font=font_panel_text)

        elif p["type"] == "peru":
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#fffbeb")
            # Text placed safely above waveform
            draw.text((dw1 + 15, dy1 + 8), "MAGNITUDE 6.7 - CENTRAL PERU", fill="#b45309", font=font_panel_title)
            # Seismograph lines starting below text
            points = [
                (dw1 + 15, dy1 + 65),
                (dw1 + 60, dy1 + 65),
                (dw1 + 85, dy1 + 35),
                (dw1 + 105, dy1 + 95),
                (dw1 + 125, dy1 + 25),
                (dw1 + 145, dy1 + 85),
                (dw1 + 165, dy1 + 65),
                (dw2 - 15, dy1 + 65)
            ]
            draw.line(points, fill="#d97706", width=4)
            draw.text((dw1 + 15, dy1 + 85), "Cinema crowds flee amid intense shaking.", fill="#78350f", font=font_panel_text)

        elif p["type"] == "gta":
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#fdf4ff")
            draw.text((dw1 + 15, dy1 + 10), "GTA VI LAUNCH", fill="#86198f", font=font_panel_title)
            # Bar chart soaring
            draw.rectangle([dw1 + 25, dy1 + 60, dw1 + 65, dy1 + 95], fill="#d8b4fe")
            draw.rectangle([dw1 + 85, dy1 + 40, dw1 + 125, dy1 + 95], fill="#c084fc")
            draw.rectangle([dw1 + 145, dy1 + 15, dw1 + 185, dy1 + 95], fill="#9333ea")
            draw.text((dw1 + 200, dy1 + 35), "ALL-TIME", fill="#6b21a8", font=font_panel_title)
            draw.text((dw1 + 200, dy1 + 55), "RECORD!", fill="#6b21a8", font=font_panel_title)

        elif p["type"] == "wallstreet":
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#fff1f2")
            draw.text((dw1 + 15, dy1 + 10), "S&P 500 / DOW JONES DROP", fill="#991b1b", font=font_panel_title)
            # Stock drop line
            chart_pts = [
                (dw1 + 15, dy1 + 35),
                (dw1 + 75, dy1 + 45),
                (dw1 + 135, dy1 + 40),
                (dw1 + 195, dy1 + 75),
                (dw1 + 255, dy1 + 90),
                (dw2 - 15, dy1 + 95)
            ]
            draw.line(chart_pts, fill="#dc2626", width=4)
            draw.text((dw1 + 205, dy1 + 55), "AI SELLOFF", fill="#991b1b", font=font_panel_title)

        # Draw description text cleanly inside bottom of panel
        draw.text((bx1 + 12, by2 - 30), p["desc"], fill="#222222", font=font_panel_text)

    # Footer note positioned cleanly inside black bar
    draw.rectangle([20, 1000, 1004, 1024], fill="#111111")
    draw.text((36, 1006), "SPECIAL EDITION -- VERIFIED WORLD REPORT -- ALL RIGHTS RESERVED", fill="#ffffff", font=font_panel_text)

    # Save
    img.save("entry.png", "PNG")
    print("entry.png regenerated successfully with fixes.")

if __name__ == "__main__":
    draw_newspaper()
