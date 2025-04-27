document.getElementById('moodForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const text = document.getElementById('userText').value;
    
    // Show loading state
    const button = e.target.querySelector('button');
    button.disabled = true;
    button.textContent = 'Analyzing...';
    
    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text })
        });
        
        const data = await response.json();
        
        // Display results
        const moodElement = document.getElementById('moodResult');
        moodElement.textContent = data.mood;
        moodElement.className = data.mood;
        
        const activityList = document.getElementById('activityList');
        activityList.innerHTML = data.activities.map(a => `<li>${a}</li>`).join('');
        
        document.getElementById('results').classList.remove('hidden');
    } catch (error) {
        alert('Error analyzing your mood. Please try again.');
    } finally {
        button.disabled = false;
        button.textContent = 'Analyze My Mood';
    }
});