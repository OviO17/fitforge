const menuToggle = document.querySelector('.menu-toggle');
const mainNavigation = document.querySelector('#main-navigation');
const profileToggle = document.querySelector('.profile-toggle');
const profileDropdown = document.querySelector('#profile-dropdown');

if (menuToggle && mainNavigation) {
    menuToggle.addEventListener('click', () => {
        const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
        menuToggle.setAttribute('aria-expanded', String(!isOpen));
        menuToggle.setAttribute('aria-label', isOpen ? 'Open navigation menu' : 'Close navigation menu');
        mainNavigation.classList.toggle('is-open', !isOpen);
    });

    mainNavigation.addEventListener('click', (event) => {
        if (event.target.closest('a')) {
            menuToggle.setAttribute('aria-expanded', 'false');
            menuToggle.setAttribute('aria-label', 'Open navigation menu');
            mainNavigation.classList.remove('is-open');
            if (profileToggle && profileDropdown) {
                profileToggle.setAttribute('aria-expanded', 'false');
                profileDropdown.classList.remove('is-open');
            }
        }
    });
}

if (profileToggle && profileDropdown) {
    profileToggle.addEventListener('click', () => {
        const isOpen = profileToggle.getAttribute('aria-expanded') === 'true';
        profileToggle.setAttribute('aria-expanded', String(!isOpen));
        profileToggle.setAttribute('aria-label', isOpen ? 'Open profile menu' : 'Close profile menu');
        profileDropdown.classList.toggle('is-open', !isOpen);
    });

    document.addEventListener('click', (event) => {
        if (!event.target.closest('.profile-menu')) {
            profileToggle.setAttribute('aria-expanded', 'false');
            profileToggle.setAttribute('aria-label', 'Open profile menu');
            profileDropdown.classList.remove('is-open');
        }
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
            profileToggle.setAttribute('aria-expanded', 'false');
            profileToggle.setAttribute('aria-label', 'Open profile menu');
            profileDropdown.classList.remove('is-open');
        }
    });
}
