/**
 * js/animations.js
 * Lightweight scroll-reveal system using IntersectionObserver
 */

document.addEventListener('DOMContentLoaded', () => {
    const revealElements = document.querySelectorAll('[data-reveal]');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add a small delay based on data-delay attribute if present
                const delay = entry.target.dataset.delay || 0;
                setTimeout(() => {
                    entry.target.classList.add('revealed');
                }, delay);
                
                // Once revealed, we can stop observing this element
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // Handle Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('navbar-scrolled', 'glass-panel');
                navbar.style.height = '70px';
                document.documentElement.style.setProperty('--nav-height', '70px');
            } else {
                navbar.classList.remove('navbar-scrolled', 'glass-panel');
                navbar.style.height = '80px';
                document.documentElement.style.setProperty('--nav-height', '80px');
            }
        });
    }
});
