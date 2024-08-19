// Function to redirect to index2.html
function redirectToIndex2() {
    window.location.href = 'index2.html';
}

function redirectToIndex3() {
    window.location.href = 'index3.html';
}

// Get the button elements by their IDs
const victoryPredictorButton = document.getElementById('victory-predictor');
const scorePredictorButton = document.getElementById('score-predictor');

// Attach click event listeners to the buttons
victoryPredictorButton.addEventListener('click', redirectToIndex2);
scorePredictorButton.addEventListener('click', redirectToIndex3);

function predictProbability() {
    // Example logic for demonstration purposes
    const battingTeam = document.getElementById('batting-team').value;
    const bowlingTeam = document.getElementById('bowling-team').value;
    const resultDiv = document.getElementById('result');
    const battingTeamResult = document.getElementById('batting-team-result');
    const bowlingTeamResult = document.getElementById('bowling-team-result');

    // Display the result div
    resultDiv.style.display = 'block';

    // Example probabilities (you should replace this with actual calculation logic)
    const battingTeamProbability = '60%';
    const bowlingTeamProbability = '40%';

    // Update the results based on the selected teams
    battingTeamResult.innerHTML = `${battingTeam}: <span>${battingTeamProbability}</span>`;
    bowlingTeamResult.innerHTML = `${bowlingTeam}: <span>${bowlingTeamProbability}</span>`;
}

function predictMatchScore() {
    // Dummy logic for match score prediction
    const currentRuns = document.getElementById('current_runs').value;
    const currentOver = document.getElementById('overs').value;
    const wicketsFallen = document.getElementById('wickets').value;
    const runsLast5 = document.getElementById('last_five_over_score').value;
    const wicketsLast5 = document.getElementById('last_five_over_wicket').value;

    // Simple prediction logic (for demonstration purposes)
    const predictedScore = parseInt(currentRuns) + (20 - parseInt(currentOver)) * (parseInt(runsLast5) / 5);

    // Display the predicted score
    const result = document.getElementById('result');
    const predictedScoreElement = document.getElementById('predicted-score').querySelector('span');
    predictedScoreElement.textContent = Math.round(predictedScore);
    result.style.display = 'block';
}