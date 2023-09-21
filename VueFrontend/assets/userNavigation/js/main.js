const menuToggle = document.querySelector('.menu-toggle')
const sidebar = document.querySelector('.sidebar')
const logo = document.querySelector('.logo-text')
const searchBox = document.querySelector('.search-box')
const searchInput = document.querySelector('.search-box input')

const dashboardText = document.querySelector('.dashboard-link span')
const petText = document.querySelector('.pets-link span')
const clientsText = document.querySelector('.clients-link span')
const vetsText = document.querySelector('.vets-link span')
const settingsText = document.querySelector('.settings-link span')

const userPhoto = document.querySelector('.user-image')
const userData = document.querySelector('.user-data')

menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('close');
    menuToggle.classList.toggle('rotate')
    logo.classList.toggle('hideElement')
    searchBox.classList.toggle('change-bg')
    searchInput.classList.toggle('hideElement')
    dashboardText.classList.toggle('hideElement')
    petText.classList.toggle('hideElement')
    clientsText.classList.toggle('hideElement')
    vetsText.classList.toggle('hideElement')
    settingsText.classList.toggle('hideElement')
    userPhoto.classList.toggle('hideElement')
    userData.classList.toggle('hideElement')

})

searchBox.addEventListener('click', () => {
    sidebar.classList.remove('close');
    menuToggle.classList.remove('rotate')
    logo.classList.remove('hideElement')
    searchBox.classList.remove('change-bg')
    searchInput.classList.remove('hideElement')
    dashboardText.classList.remove('hideElement')
    petText.classList.remove('hideElement')
    clientsText.classList.remove('hideElement')
    vetsText.classList.remove('hideElement')
    settingsText.classList.remove('hideElement')
    userPhoto.classList.remove('hideElement')
    userData.classList.remove('hideElement')
})