export default function Home() {
  return (
    <div style={{fontFamily:'Arial, sans-serif', background:'#ffffff', color:'#000', padding:'40px'}}>
      <h1 style={{fontSize:'48px', marginBottom:'10px'}}>Kori Pickle</h1>
      <h2 style={{color:'#FF8200'}}>Healthcare Revenue Cycle Workflow Portfolio</h2>
      <p>RCM Case Studies | Denial Prevention | Claims Analysis | Health Informatics</p>
    </div>
  )
}

export const metadata = {
  title: 'Healthcare Revenue Cycle Workflow Portfolio',
  description: 'RCM Case Studies | Denial Prevention | Claims Analysis | Health Informatics',
  openGraph: {
    title: 'Healthcare Revenue Cycle Workflow Portfolio',
    description: 'RCM Case Studies | Denial Prevention | Claims Analysis | Health Informatics',
    images: ['/api/og'],
  },
};