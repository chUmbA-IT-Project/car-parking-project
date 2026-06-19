// ===== Mobile Menu Toggle =====
document.addEventListener('DOMContentLoaded', function() {
    const burgerBtn = document.getElementById('burgerBtn');
    const mobileMenu = document.getElementById('mobileMenu');

    if (burgerBtn && mobileMenu) {
        burgerBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
            burgerBtn.classList.toggle('active');
        });

        // Close mobile menu on link click
        mobileMenu.querySelectorAll('.mobile-menu__link').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.remove('active');
                burgerBtn.classList.remove('active');
            });
        });
    }

    // ===== Messages Auto-close =====
    document.querySelectorAll('.message__close').forEach(btn => {
        btn.addEventListener('click', function() {
            this.closest('.message').remove();
        });
    });

    // Auto-close messages after 5 seconds
    document.querySelectorAll('.message').forEach(msg => {
        setTimeout(() => {
            if (msg) {
                msg.style.transition = 'opacity 0.5s ease';
                msg.style.opacity = '0';
                setTimeout(() => msg.remove(), 500);
            }
        }, 5000);
    });

    // ===== Password Toggle =====
    const passwordToggle = document.getElementById('passwordToggle');
    const passwordInput = document.getElementById('loginPassword');
    const passwordIcon = document.getElementById('passwordIcon');

    if (passwordToggle && passwordInput) {
        passwordToggle.addEventListener('click', function() {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            passwordIcon.classList.toggle('fa-eye');
            passwordIcon.classList.toggle('fa-eye-slash');
        });
    }

    // ===== Hero Carousel =====
    const carousel = document.getElementById('heroCarousel');
    const prevBtn = document.getElementById('heroPrev');
    const nextBtn = document.getElementById('heroNext');
    const dotsContainer = document.getElementById('heroDots');

    if (carousel) {
        const slides = carousel.querySelectorAll('.hero__slide');
        const dots = dotsContainer ? dotsContainer.querySelectorAll('.hero__dot') : [];
        let currentSlide = 0;
        let autoPlayInterval;

        function showSlide(index) {
            slides.forEach(slide => slide.classList.remove('active'));
            dots.forEach(dot => dot.classList.remove('active'));
            
            currentSlide = (index + slides.length) % slides.length;
            slides[currentSlide].classList.add('active');
            if (dots[currentSlide]) {
                dots[currentSlide].classList.add('active');
            }
        }

        function nextSlide() {
            showSlide(currentSlide + 1);
        }

        function prevSlide() {
            showSlide(currentSlide - 1);
        }

        function startAutoPlay() {
            stopAutoPlay();
            autoPlayInterval = setInterval(nextSlide, 5000);
        }

        function stopAutoPlay() {
            if (autoPlayInterval) {
                clearInterval(autoPlayInterval);
                autoPlayInterval = null;
            }
        }

        if (slides.length > 1) {
            // Event Listeners
            if (prevBtn) {
                prevBtn.addEventListener('click', () => {
                    prevSlide();
                    startAutoPlay();
                });
            }

            if (nextBtn) {
                nextBtn.addEventListener('click', () => {
                    nextSlide();
                    startAutoPlay();
                });
            }

            // Dot navigation
            if (dots.length > 0) {
                dots.forEach(dot => {
                    dot.addEventListener('click', function() {
                        const index = parseInt(this.getAttribute('data-index'));
                        showSlide(index);
                        startAutoPlay();
                    });
                });
            }

            // Keyboard navigation
            document.addEventListener('keydown', function(e) {
                if (e.key === 'ArrowLeft') {
                    prevSlide();
                    startAutoPlay();
                } else if (e.key === 'ArrowRight') {
                    nextSlide();
                    startAutoPlay();
                }
            });

            // Touch/Swipe support
            let touchStartX = 0;
            let touchEndX = 0;

            carousel.addEventListener('touchstart', function(e) {
                touchStartX = e.changedTouches[0].screenX;
            }, { passive: true });

            carousel.addEventListener('touchend', function(e) {
                touchEndX = e.changedTouches[0].screenX;
                handleSwipe();
            }, { passive: true });

            function handleSwipe() {
                const swipeThreshold = 50;
                const diff = touchStartX - touchEndX;
                
                if (Math.abs(diff) > swipeThreshold) {
                    if (diff > 0) {
                        nextSlide();
                    } else {
                        prevSlide();
                    }
                    startAutoPlay();
                }
            }

            // Start autoplay
            startAutoPlay();

            // Pause on hover
            carousel.addEventListener('mouseenter', stopAutoPlay);
            carousel.addEventListener('mouseleave', startAutoPlay);
        }
    }
});