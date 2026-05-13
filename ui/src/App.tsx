import { useState } from 'react'
import UploadForm from './compnents/UploadForm'
import AskForm from './compnents/AskForm'

function App() {
  const [docId, setDocId] = useState('')
  return (
    <>
      <UploadForm onIndexed = {setDocId} />
      <AskForm docId={docId} />
    </>
  )
}

export default App



