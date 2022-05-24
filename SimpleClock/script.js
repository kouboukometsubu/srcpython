


setInterval(() => {
    const timeText = new Date().toLocaleDateString("ja-JP");
    document.querySelector("#currentTime").textContent = timeText ;
}, 1000)