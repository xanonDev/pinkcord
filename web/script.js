document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        const elements = document.querySelectorAll('[style*="display: none;"]');
        let delay = 0;
        const skipbtn = document.getElementById("skip");
        scrollYN = true;

        skipbtn.addEventListener('click', function() {
            scrollYN = false;
            elements.forEach(element => {
                element.style.display = "block";
            });
        });

        function getRandomArbitrary(min, max) {
            return Math.random() * (max - min) + min;
        }

        elements.forEach(element => {
            setTimeout(() => {
                element.style.display = "block";
                if (scrollYN === true) {
                    element.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }, delay);
            delay += getRandomArbitrary(300, 1000);
        });
    }, 1111);
});
