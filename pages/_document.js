import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html>
      <Head>
        <title>Revenue Cycle Optimization Portfolio | Kori Pickle</title>
        <meta name="description" content="Self-directed RCM case studies focused on denial prevention, claims analysis, eligibility workflows, healthcare operations, and workflow intelligence. No PHI, no employer data, and no false work claims are used." />
        <meta name="author" content="Kori Pickle" />
        <meta property="og:title" content="Revenue Cycle Optimization Portfolio" />
        <meta property="og:description" content="Self-directed RCM case studies focused on denial prevention, claims analysis, eligibility workflows, healthcare operations, and workflow intelligence. No PHI, no false work claims." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://healthcare-workflow-portfolio.vercel.app/" />
        <meta property="og:image" content="https://healthcare-workflow-portfolio.vercel.app/api/og.png" />
        <meta property="og:image:secure_url" content="https://healthcare-workflow-portfolio.vercel.app/api/og.png" />
        <meta property="og:image:type" content="image/png" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Revenue Cycle Optimization Portfolio" />
        <meta name="twitter:description" content="Self-directed RCM case studies focused on denial prevention, claims analysis, eligibility workflows, and healthcare operations." />
        <meta name="twitter:image" content="https://healthcare-workflow-portfolio.vercel.app/api/og.png" />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
