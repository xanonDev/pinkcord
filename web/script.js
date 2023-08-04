document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        const elements = document.querySelectorAll('[style*="display: none;"]');
        let delay = 0;

        function getRandomArbitrary(min, max) {
            return Math.random() * (max - min) + min;
        }

        elements.forEach(element => {
            setTimeout(() => {
                element.style.display = "block";
                element.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, delay);
            delay += getRandomArbitrary(300, 1000);
        });
    }, 1111);
});