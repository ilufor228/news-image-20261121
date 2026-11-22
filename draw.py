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
    
    font_masthead = ImageFont.truetype(font_path, 46)
    font_subhead = ImageFont.truetype(font_path, 16)
    font_panel_title = ImageFont.truetype(font_path, 15)
    font_panel_text = ImageFont.truetype(font_path, 12)

    # Header section
    draw.rectangle([20, 20, 1004, 130], fill="#111111")
    draw.text((36, 32), "THE GLOBAL CHRONICLE", fill="#ffffff", font=font_masthead)
    draw.text((36, 88), "SATURDAY, 21 NOVEMBER 2026  |  WORLD EDITION", fill="#e0e0e0", font=font_subhead)
    draw.text((740, 88), "PRICE: $2.50", fill="#e0e0e0", font=font_subhead)

    # Thin separator line
    draw.rectangle([20, 140, 1004, 145], fill="#111111")

    # Panels configuration (3 rows, 2 columns)
    # Grid: 
    # Left col: x = 20 to 502
    # Right col: x = 522 to 1004
    # Rows: 
    # R1: y = 155 to 435
    # R2: y = 450 to 730
    # R3: y = 745 to 1025 (adjusted slightly to fit 1024)

    panels = [
        {
            "box": (20, 155, 502, 435),
            "title": "IRAN STRIKES US SITES IN BAHRAIN",
            "desc": "Missile strikes hit US radar & base in Bahrain; F-16 fighter damaged as Middle East tensions surge.",
            "type": "iran"
        },
        {
            "box": (522, 155, 1004, 435),
            "title": "COP31 DEADLOCK IN ANTALYA",
            "desc": "Climate summit in Antalya, Turkey overruns deadline amid bitter deadlock over fossil fuel phaseout.",
            "type": "cop31"
        },
        {
            "box": (20, 450, 502, 730),
            "title": "FBI DATABASE HACKED",
            "desc": "FBI investigates massive breach into US national criminal database used by police nationwide.",
            "type": "fbi"
        },
        {
            "box": (522, 450, 1004, 730),
            "title": "PERU EARTHQUAKE 6.7",
            "desc": "Powerful magnitude 6.7 earthquake strikes central Peru, sending panicked crowds fleeing cinemas.",
            "type": "peru"
        },
        {
            "box": (20, 745, 502, 1020),
            "title": "GTA VI SMASHES RECORDS",
            "desc": "Grand Theft Auto VI launches to unprecedented numbers, shattering all historical entertainment records.",
            "type": "gta"
        },
        {
            "box": (522, 745, 1004, 1020),
            "title": "WALL STREET SLIDES",
            "desc": "US stocks plunge in AI stock sell-off; S&P 500 and Dow Jones enter deep market correction.",
            "type": "wallstreet"
        }
    ]

    for p in panels:
        bx1, by1, bx2, by2 = p["box"]
        # Panel container box
        draw.rectangle([bx1, by1, bx2, by2], outline="#333333", width=2, fill="#ffffff")
        # Panel title banner
        draw.rectangle([bx1, by1, bx2, by1 + 32], fill="#222222")
        draw.text((bx1 + 12, by1 + 8), p["title"], fill="#ffffff", font=font_panel_title)

        # Drawing area inside panel
        dw1, dy1, dw2, dy2 = bx1 + 12, by1 + 42, bx2 - 12, by2 - 45
        
        # Draw custom illustrations based on panel type
        if p["type"] == "iran":
            # Missile & Base graphic
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#f5f5f5")
            # Base icon
            draw.rectangle([dw1 + 30, dy2 - 50, dw1 + 130, dy2 - 10], fill="#444")
            draw.text((dw1 + 38, dy2 - 42), "US BASE", fill="#fff", font=font_panel_text)
            # Radar dish
            draw.arc([dw1 + 160, dy2 - 70, dw1 + 220, dy2 - 10], start=180, end=360, fill="#222", width=3)
            draw.line([dw1 + 190, dy2 - 40, dw1 + 190, dy2 - 10], fill="#222", width=3)
            # Missile arc
            draw.line([dw2 - 40, dy1 + 20, dw1 + 110, dy2 - 30], fill="#cc0000", width=4)
            # Explosion star
            draw.ellipse([dw1 + 90, dy2 - 50, dw1 + 130, dy2 - 10], fill="#ff6600")
            draw.text((dw1 + 150, dy1 + 15), "F-16 HIT", fill="#cc0000", font=font_panel_title)

        elif p["type"] == "cop31":
            # Climate summit deadlock
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#eef2f5")
            draw.rectangle([dw1 + 20, dy1 + 15, dw1 + 240, dy1 + 45], fill="#1b4332")
            draw.text((dw1 + 30, dy1 + 22), "COP31 ANTALYA", fill="#ffffff", font=font_panel_title)
            # Scales of deadlock
            draw.line([dw1 + 130, dy1 + 55, dw1 + 130, dy1 + 110], fill="#333", width=3)
            draw.line([dw1 + 80, dy1 + 70, dw1 + 180, dy1 + 70], fill="#333", width=3)
            draw.rectangle([dw1 + 60, dy1 + 70, dw1 + 90, dy1 + 90], fill="#d90429")
            draw.rectangle([dw1 + 170, dy1 + 70, dw1 + 200, dy1 + 90], fill="#2b9348")
            draw.text((dw1 + 100, dy1 + 95), "DEADLOCK", fill="#d90429", font=font_panel_title)

        elif p["type"] == "fbi":
            # FBI database hacked
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#111827")
            draw.rectangle([dw1 + 20, dy1 + 15, dw1 + 200, dy1 + 95], outline="#ef4444", width=3, fill="#1f2937")
            draw.text((dw1 + 30, dy1 + 25), "FBI DATABASE", fill="#9ca3af", font=font_panel_text)
            draw.text((dw1 + 30, dy1 + 45), "BREACHED!", fill="#ef4444", font=font_panel_title)
            # Binary stream
            draw.text((dw1 + 215, dy1 + 20), "010068 110101", fill="#10b981", font=font_panel_text)
            draw.text((dw1 + 215, dy1 + 45), "SQL INJECTION", fill="#ef4444", font=font_panel_text)
            draw.text((dw1 + 215, dy1 + 70), "ALERT: SEC_FAIL", fill="#f59e0b", font=font_panel_text)

        elif p["type"] == "peru":
            # Peru earthquake 6.7
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#fffbeb")
            draw.text((dw1 + 20, dy1 + 15), "MAGNITUDE 6.7", fill="#b45309", font=font_panel_title)
            # Seismograph lines
            points = [
                (dw1 + 20, dy1 + 65),
                (dw1 + 70, dy1 + 65),
                (dw1 + 90, dy1 + 30),
                (dw1 + 110, dy1 + 100),
                (dw1 + 130, dy1 + 20),
                (dw1 + 150, dy1 + 90),
                (dw1 + 170, dy1 + 65),
                (dw2 - 20, dy1 + 65)
            ]
            draw.line(points, fill="#d97706", width=4)
            draw.text((dw1 + 20, dy1 + 95), "CENTRAL PERU - CINEMA PANIC", fill="#78350f", font=font_panel_text)

        elif p["type"] == "gta":
            # GTA VI records
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#fdf4ff")
            draw.text((dw1 + 20, dy1 + 15), "GTA VI LAUNCH", fill="#86198f", font=font_panel_title)
            # Bar chart soaring
            draw.rectangle([dw1 + 30, dy1 + 80, dw1 + 70, dy1 + 110], fill="#d8b4fe")
            draw.rectangle([dw1 + 90, dy1 + 60, dw1 + 130, dy1 + 110], fill="#c084fc")
            draw.rectangle([dw1 + 150, dy1 + 25, dw1 + 190, dy1 + 110], fill="#9333ea")
            draw.text((dw1 + 210, dy1 + 35), "ALL-TIME", fill="#6b21a8", font=font_panel_title)
            draw.text((dw1 + 210, dy1 + 60), "RECORD!", fill="#6b21a8", font=font_panel_title)

        elif p["type"] == "wallstreet":
            # Wall street slides
            draw.rectangle([dw1, dy1, dw2, dy2], fill="#fff1f2")
            draw.text((dw1 + 20, dy1 + 15), "S&P 500 / DOW JONES", fill="#991b1b", font=font_panel_title)
            # Stock drop line
            chart_pts = [
                (dw1 + 20, dy1 + 35),
                (dw1 + 80, dy1 + 45),
                (dw1 + 140, dy1 + 40),
                (dw1 + 200, dy1 + 85),
                (dw1 + 260, dy1 + 105),
                (dw2 - 20, dy1 + 110)
            ]
            draw.line(chart_pts, fill="#dc2626", width=4)
            draw.text((dw1 + 210, dy1 + 70), "AI SELLOFF", fill="#991b1b", font=font_panel_title)

        # Draw description text at the bottom of panel
        # Wrap or draw text
        draw.text((bx1 + 12, by2 - 38), p["desc"], fill="#222222", font=font_panel_text)

    # Footer note
    draw.rectangle([20, 995, 1004, 1015], fill="#111111")
    draw.text((36, 1000), "SPECIAL EDITION -- VERIFIED WORLD REPORT -- ALL RIGHTS RESERVED", fill="#ffffff", font=font_panel_text)

    # Save
    img.save("entry.png", "PNG")
    print("entry.png generated successfully.")

if __name__ == "__main__":
    draw_newspaper()
