 
import base64
from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def generate_pdf_report(scan_data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#8b5cf6'),
        alignment=1,
        spaceAfter=30
    )
    story.append(Paragraph("🛡️ AI QR Shield - Security Report", title_style))
    
    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.grey,
        alignment=2,
    )
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}", date_style))
    story.append(Spacer(1, 20))
    
    result_color = colors.HexColor('#10b981') if scan_data['result'] == 'SAFE' else colors.HexColor('#f59e0b') if scan_data['result'] == 'SUSPICIOUS' else colors.HexColor('#ef4444')
    
    result_style = ParagraphStyle(
        'ResultStyle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=result_color,
        spaceAfter=10
    )
    story.append(Paragraph(f"Result: {scan_data['result']}", result_style))
    
    data = [
        ['Metric', 'Value'],
        ['Category', scan_data['type']],
        ['Security Level', scan_data['security_level']],
        ['Risk Score', f"{scan_data['risk_score']}/100"],
        ['AI Confidence', f"{scan_data['confidence']:.1f}%"],
    ]
    
    table = Table(data, colWidths=[2*inch, 4*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8b5cf6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f5f0ff')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#4c1d95')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e9d5ff'))
    ]))
    story.append(table)
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("📄 QR Content", styles['Heading2']))
    qr_style = ParagraphStyle(
        'QRCodeStyle',
        parent=styles['Code'],
        fontSize=8,
        backColor=colors.HexColor('#f5f0ff'),
        borderColor=colors.HexColor('#e9d5ff'),
        borderWidth=1,
        borderPadding=10,
        spaceAfter=10
    )
    story.append(Paragraph(scan_data['data'], qr_style))
    story.append(Spacer(1, 10))
    
    if 'reasons' in scan_data and scan_data['reasons']:
        story.append(Paragraph("🔍 Analysis Details", styles['Heading2']))
        for reason in scan_data['reasons']:
            story.append(Paragraph(f"• {reason}", styles['Normal']))
        story.append(Spacer(1, 10))
    
    doc.build(story)
    buffer.seek(0)
    return buffer