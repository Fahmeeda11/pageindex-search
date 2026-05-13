import { useState } from 'react'
import { askQuestion } from '../api'

function AskForm({ docId} : { docId: string}) {
    const [ question, setQuestion] = useState('')
    const [ answer, setAnswer] = useState('')

    async function handleAsk() {
        setAnswer('thinking...')
        const result = await askQuestion(docId, question)
        setAnswer(result.answer)
    }
    return (
        <>
            <textarea value={question} onChange={(e) =>
                setQuestion(e.target.value)
            } />
            <button onClick={handleAsk}>Ask</button>
            <p>{answer}</p>
        </>
    )
}
export default AskForm