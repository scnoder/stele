async function analyze() {
    const url = document.getElementById('urlInput').value.trim();
    if (!url) return;

    const btn = document.getElementById('analyzeBtn');
    const status = document.getElementById('status');
    const analysisSection = document.getElementById('analysisSection');
    const transcriptSection = document.getElementById('transcriptSection');
    const analysisBox = document.getElementById('analysisBox');
    const transcriptBox = document.getElementById('transcriptBox');

    btn.disabled = true;
    status.style.display = 'block';
    analysisSection.style.display = 'none';
    transcriptSection.style.display = 'none';
    analysisBox.className = 'result-box';

    try {
        const res = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });
        const data = await res.json();

        status.style.display = 'none';
        analysisSection.style.display = 'block';

        if (data.error) {
            analysisBox.className = 'result-box error';
            analysisBox.textContent = data.error;
        } else {
            analysisBox.textContent = data.result;
            if (data.transcript) {
                transcriptSection.style.display = 'block';
                transcriptBox.textContent = data.transcript;
            }
        }
    } catch (e) {
        status.style.display = 'none';
        analysisSection.style.display = 'block';
        analysisBox.className = 'result-box error';
        analysisBox.textContent = 'Network error: ' + e.message;
    }

    btn.disabled = false;
}

document.getElementById('urlInput').addEventListener('keydown', e => {
    if (e.key === 'Enter') analyze();
});