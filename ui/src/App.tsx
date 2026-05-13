import { useState } from 'react'
import UploadForm from './compnents/UploadForm'

function App() {
  const [docId, setDocId] = useState('')
  return (
    <>
      <UploadForm onIndexed = {setDocId} />
      <p>docId: {docId}</p>
    </>
  )
}

export default App



