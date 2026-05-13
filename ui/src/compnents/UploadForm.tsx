import { useState} from 'react'
import { uploadFile} from '../api'

// #declaring a component that takes a prop onIndexed 
//what shape it must pass

function UploadForm({ onIndexed }: {
    onIndexed: (id: string) => void}) { 
// #usestate is a container or a space to store data, here in this case
// #there is a container for file and a container for message.
        const [file, setFile] = useState<File | null>(null) //this container only has file or null
        const [message, setMessage] = useState('') //this container starts empty


        async function handleUpload() {
            if (!file) return
            setMessage('Uploading...')
            const result = await uploadFile(file)
            setMessage('done:' + result.doc_id)
            onIndexed(result.doc_id)
}
        return (
            <>
                <input type="file" accept="application/pdf" onChange={(e) => 
                    setFile(e.target.files?.[0] ?? null)} />
                    <button onClick={handleUpload}>Upload</button>
                    <p>{message}</p>
            </>
            )
        }
export default UploadForm





