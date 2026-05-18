import { useState } from 'react'
import UploadForm from './compnents/UploadForm'
import AskForm from './compnents/AskForm'
import { Layout, Card } from 'antd'

function App() {
  const [docId, setDocId] = useState('')
  return (
    <Layout style={{ minHeight: '100vh', background: '#1c1d1d' }}>
      <Layout.Header style={{ color: 'white', fontSize: 24, background: '#1c1d1d' }}>
        Hey, upload your PDF and ask questions about it!
      </Layout.Header>
      <Layout.Content style={{ maxWidth: 700, margin: '0 auto', padding: 24 }}>
        <Card style={{ marginBottom: 24, background: '#2c2d2d' }}>
          <UploadForm onIndexed = {setDocId} />
          <AskForm docId={docId} />
        </Card>
        </Layout.Content>
    </Layout>
  )
}

export default App



