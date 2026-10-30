# Macht aus den Mailfolge-Vorlagen eine Fassung für Brevos Drag-and-drop-Editor:
# Fusszeile in die Hauptkarte, Aufzählungs-Tabellen als Absätze, Button markiert, versteckter Vorschautext entfernt.
import re, sys

OUT = '/home/claude/baustelle-buero/mail/'
P = "margin:0 0 12px 0;font-family:'Red Hat Text', Arial, Helvetica, sans-serif;font-size:16px;line-height:24px;color:#13232B;"

def lists_to_p(html):
    def repl(m):
        rows = re.findall(r'<tr><td valign="top"[^>]*>(.*?)</td><td[^>]*>(.*?)</td></tr>', m.group(0), re.S)
        out = []
        for marker, text in rows:
            num = re.sub(r'<[^>]+>', '', marker).strip()
            prefix = f'<strong style="color:#0E5A6B;">{num}.</strong> ' if num.isdigit() else '<strong style="color:#E2762A;">–</strong> '
            out.append(f'<p style="{P}">{prefix}{text}</p>')
        return ''.join(out)
    return re.sub(r'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 16px 0;">.*?</table>', repl, html, flags=re.S)

def convert(html):
    html = re.sub(r'<div style="display:none;.*?</div>\n', '', html, count=1, flags=re.S)
    html = lists_to_p(html)
    footer_join = re.compile(r'(      </td></tr>\n)    </table>\n    <table role="presentation" width="600" class="card"[^>]*>\n')
    html, n = footer_join.subn(r'\1', html, count=1)
    assert n == 1, 'Fusszeile nicht gefunden'
    html = html.replace('<td align="center" bgcolor=', '<td data-role="cta-primary" align="center" bgcolor=')
    return html

for nr in (1, 2, 3):
    src = open(f'{OUT}toolkit-folge-{nr}.html', encoding='utf-8').read()
    open(f'{OUT}toolkit-folge-{nr}-brevo.html', 'w', encoding='utf-8').write(convert(src))
print('ok')
