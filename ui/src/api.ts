export async function uploadFile(file: File) {
    const formData = new FormData();
    formData.append('pdf', file);
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    return response.json();
}

export async function askQuestion(docId: string, question: string) {
    const response = await fetch('/ask', {
        method: 'POST',
        headers: 
        { 'Content-Type': 'application/json'},
        body : JSON.stringify({ doc_id: docId, question })
    });
    return response.json();
}