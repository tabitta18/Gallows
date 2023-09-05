eel.expose(updateDisplay);
function updateDisplay(word, attemptsLeft) {
    document.getElementById("word-display").innerText = word;
    document.getElementById("attempts-left").innerText = attemptsLeft;
}

function makeGuess() {
    const guess = document.getElementById("guess").value;
    eel.make_guess(guess)();
}
