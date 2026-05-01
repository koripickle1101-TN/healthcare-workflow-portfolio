export default function handler(req, res) {
  const svg = `
  <svg width="1200" height="630" viewBox="0 0 1200 630" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="630" fill="#FFFFFF"/>
    <rect x="0" y="0" width="1200" height="16" fill="#FF8200"/>
    <rect x="0" y="614" width="1200" height="16" fill="#FF8200"/>
    <line x1="80" y1="86" x2="1120" y2="86" stroke="#FF8200" stroke-width="3"/>
    <circle cx="600" cy="86" r="9" fill="#FF8200"/>
    <text x="80" y="150" fill="#FF8200" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="800" letter-spacing="8">KORI PICKLE</text>
    <text x="80" y="255" fill="#000000" font-family="Georgia, Times New Roman, serif" font-size="78" font-weight="700">Healthcare Revenue</text>
    <text x="80" y="340" fill="#000000" font-family="Georgia, Times New Roman, serif" font-size="78" font-weight="700">Cycle Portfolio</text>
    <rect x="82" y="380" width="330" height="8" fill="#FF8200"/>
    <text x="80" y="445" fill="#000000" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="800">RCM Case Studies • Denial Prevention • Claims Analysis</text>
    <text x="80" y="505" fill="#333333" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="700">Workflow analysis without false work claims or PHI</text>
    <path d="M760 344 C815 250, 874 445, 934 320 S1040 245, 1120 330" stroke="#FF8200" stroke-width="8" stroke-linecap="round"/>
    <path d="M760 470 H820 L850 310 L900 520 L950 395 H1010 L1045 280 L1085 470 H1130" stroke="#000000" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="760" cy="470" r="11" fill="#FF8200"/>
    <circle cx="820" cy="470" r="11" fill="#FF8200"/>
    <circle cx="850" cy="310" r="11" fill="#FF8200"/>
    <circle cx="900" cy="520" r="11" fill="#FF8200"/>
    <circle cx="950" cy="395" r="11" fill="#FF8200"/>
    <circle cx="1010" cy="395" r="11" fill="#FF8200"/>
    <circle cx="1045" cy="280" r="11" fill="#FF8200"/>
    <circle cx="1085" cy="470" r="11" fill="#FF8200"/>
    <circle cx="1130" cy="470" r="11" fill="#FF8200"/>
  </svg>`;
  res.setHeader('Content-Type', 'image/svg+xml');
  res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
  res.status(200).send(svg);
}
