document.addEventListener('DOMContentLoaded', function() {
    const uploadBtn = document.getElementById('upload-btn');
    const askBtn = document.getElementById('ask-btn');
    const pdfUpload = document.getElementById('pdf-upload');
    const questionInput = document.getElementById('question-input');
    const answerText = document.getElementById('answer-text');
    const uploadStatus = document.getElementById('upload-status');

    uploadBtn.addEventListener('click', async function() {
        const file = pdfUpload.files[0];
        if (!file) {
            alert('Please select a PDF file first');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            uploadStatus.textContent = 'Uploading and processing PDF...';
            const response = await fetch('http://localhost:8000/upload_pdf', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            uploadStatus.textContent = result.message;
        } catch (error) {
            console.error('Error uploading PDF:', error);
            uploadStatus.textContent = 'Error uploading PDF: ' + error.message;
        }
    });

    askBtn.addEventListener('click', async function() {
        const question = questionInput.value.trim();
        if (!question) {
            alert('Please enter a question');
            return;
        }

        try {
            answerText.textContent = 'Thinking...';
            const response = await fetch('http://localhost:8000/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            answerText.textContent = result.answer;
        } catch (error) {
            console.error('Error asking question:', error);
            answerText.textContent = 'Error getting answer: ' + error.message;
        }
    });
});