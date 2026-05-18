import { useState } from 'react'
import { askQuestion } from '../api'
import { Button, Input, Typography } from 'antd'

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
            <Typography.Paragraph>{answer}</Typography.Paragraph>
            <div style={{ display: 'flex', gap:8, alignItems: 'flex-end' }}>
                <Input.TextArea rows={4} value={question} onChange={(e) =>
                setQuestion(e.target.value)} />
                <Button type="primary" onClick={handleAsk}>Ask</Button>
            </div>
            
        </>
    )
}
export default AskForm