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
        const applyNavbarState = () => {
            const isScrolled = window.scrollY > 50;
            navbar.classList.toggle('navbar-scrolled', isScrolled);
            document.documentElement.style.setProperty('--nav-height', isScrolled ? '70px' : '80px');
        };

        let ticking = false;
        window.addEventListener('scroll', () => {
            if (ticking) return;
            ticking = true;
            window.requestAnimationFrame(() => {
                applyNavbarState();
                ticking = false;
            });
        });

        window.addEventListener('resize', applyNavbarState);
        applyNavbarState();
    }
});
