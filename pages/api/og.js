export default function handler(req, res) {
  const svg = `
  <svg width="1200" height="630" viewBox="0 0 1200 630" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="630" fill="#FFFFFF"/>
    <rect x="0" y="0" width="1200" height="18" fill="#FF8200"/>
    <rect x="0" y="612" width="1200" height="18" fill="#FF8200"/>
    <rect x="70" y="70" width="1060" height="490" rx="34" fill="#FFFFFF" stroke="#F0E8DD" stroke-width="3"/>
    <line x1="105" y1="118" x2="1095" y2="118" stroke="#FF8200" stroke-width="3"/>
    <text x="105" y="105" fill="#FF8200" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="900" letter-spacing="7">KORI PICKLE</text>

    <text x="105" y="225" fill="#000000" font-family="Georgia, Times New Roman, serif" font-size="68" font-weight="700">Revenue Cycle</text>
    <text x="105" y="302" fill="#000000" font-family="Georgia, Times New Roman, serif" font-size="68" font-weight="700">Optimization Portfolio</text>
    <rect x="108" y="334" width="390" height="9" fill="#FF8200"/>

    <text x="105" y="405" fill="#000000" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="900">Denial Prevention • Claims Analysis • Workflow Intelligence</text>
    <text x="105" y="468" fill="#333333" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="700">Self-directed RCM case studies showing workflow thinking</text>
    <text x="105" y="512" fill="#333333" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700">No PHI • No false work claims • Built for recruiter review</text>

    <path d="M775 318 C825 228, 882 420, 940 300 S1042 224, 1110 310" stroke="#FF8200" stroke-width="8" stroke-linecap="round"/>
    <path d="M775 455 H830 L860 292 L905 500 L955 380 H1010 L1045 258 L1083 455 H1120" stroke="#000000" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="775" cy="455" r="11" fill="#FF8200"/>
    <circle cx="830" cy="455" r="11" fill="#FF8200"/>
    <circle cx="860" cy="292" r="11" fill="#FF8200"/>
    <circle cx="905" cy="500" r="11" fill="#FF8200"/>
    <circle cx="955" cy="380" r="11" fill="#FF8200"/>
    <circle cx="1010" cy="380" r="11" fill="#FF8200"/>
    <circle cx="1045" cy="258" r="11" fill="#FF8200"/>
    <circle cx="1083" cy="455" r="11" fill="#FF8200"/>
    <circle cx="1120" cy="455" r="11" fill="#FF8200"/>
  </svg>`;
  res.setHeader('Content-Type', 'image/svg+xml');
  res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
  res.status(200).send(svg);
}
