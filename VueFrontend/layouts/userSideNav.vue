<template>
    
      <nav class="sidebar">
        <header>
            <div class="logo-text">
                <img src="assets/logo.svg" alt="logo">
            </div>

            <img class="menu-toggle" src="assets/menu.svg" alt="menu">
        </header>

        <div class="menu-links">
            <li class="search-box">
                <img src="assets/search.svg" alt="search-image">
                <input type="search" placeholder="Search">
            </li>
            <ul class="links-list">
                <li class="dashboard-link">
                    <a href="#">
                        <img class="icon" src="assets/grid.svg" alt="dashboard">
                        <span>Dashboard</span>
                    </a>
                </li>
                <li class="pets-link">
                    <a href="#">
                        <img class="icon" src="assets/pet.svg" alt="dashboard">
                        <span>Pets</span>
                    </a>
                </li>
                <li class="clients-link">
                    <a href="#">
                        <img class="icon" src="assets/user.svg" alt="dashboard">
                        <span>Clients</span>
                    </a>
                </li>
                <li class="vets-link">
                    <a href="#">
                        <img class="icon" src="assets/vet.svg" alt="dashboard">
                        <span>Vets</span>
                    </a>
                </li>
                <li class="settings-link">
                    <a href="#">
                        <img class="icon" src="assets/settings.svg" alt="dashboard">
                        <span>Settings</span>
                    </a>
                </li>
            </ul>
        </div>
        
        <div class="bottom-content">
            <div class="user-image">
                <img src="assets/photo.jpg" alt="user-image">
            </div>
            <div class="user-data">
                <span class="user-name">
                    John Doe
                </span>
                <span class="user-status">
                    Veterinary
                </span>
            </div>

            <img class="logout" src="assets/log-out.svg" alt="logout">
        </div>
    </nav>

    <section>
        <h1>Dashboard</h1>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sapiente deserunt hic, dolorum quis quia voluptate vel voluptas consequuntur, numquam eveniet, fugiat corrupti. Earum possimus consectetur temporibus. Rerum amet eaque nam repellat tempora perferendis ipsa, hic harum porro a, alias, expedita minus suscipit ea odio odit doloremque quod perspiciatis. Autem laboriosam minus quam. Maiores, quibusdam neque fugiat veniam mollitia illum numquam molestias incidunt, facere veritatis cumque. Eum perspiciatis reprehenderit fuga quaerat, soluta doloribus rem similique quas odit dignissimos. Doloribus soluta consequuntur culpa commodi quae odio totam, laudantium repellendus reiciendis, minus vitae velit porro! Amet, eum nulla. Numquam.</p>
    </section>
    <div class="sidenav">
        <NuxtLink to="/resume/start">Lets start</NuxtLink>
        <NuxtLink to="/resume/profile"><i class="bi bi-person"></i>{{' '}}Profile</NuxtLink>
        <NuxtLink to="/resume/education"><i class="bi bi-book"></i>{{' '}}Education</NuxtLink>
        <NuxtLink to="/resume/experience"><i class="bi bi-list-stars"></i>{{' '}}Experience</NuxtLink>
        <NuxtLink to="/resume/language"><i class="bi bi-translate"></i>{{' '}}Languages</NuxtLink>
        <NuxtLink to="/resume/certification"><i class="bi bi-patch-check"></i>{{' '}}Certification</NuxtLink>
        <NuxtLink to="/resume/project"><i class="bi bi-blockquote-left"></i>{{' '}}Projects</NuxtLink>
        <NuxtLink to="/resume/referee"><i class="bi bi-sliders2"></i>{{' '}}Referees</NuxtLink>
        <NuxtLink to="/template"><i class="bi bi-eye-fill"></i>{{' '}}Preview</NuxtLink>
    </div>
    <div class="main py-4 d-flex justify-contents-center">
            <slot />
    </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import axiosT from 'axios';

definePageMeta({
  layout: "template3",
})


export default defineComponent({
  name: 'fetchData',
  setup() {
    const users = ref([]);
    const template3 = ref('');
    const pdfContent = ref('');
    const user_id = 1;
    const axios = useNuxtApp().$axios;

    const generatePDF = async () => {
      
      const content = pdfContent.value;

      try {
        const response = await axiosT.post('http://localhost:3000/generate-pdf', {
          html: content.innerHTML,
        }, {
          responseType: 'blob',
        });

        const blobUrl = URL.createObjectURL(response.data);
        const link = document.createElement('a');
        link.href = blobUrl;
        link.download = 'generated-pdf.pdf';
        link.click();

        URL.revokeObjectURL(blobUrl);
      } catch (error) {
        console.error('PDF generation error:', error);
      }
    }

    const fetchData = async () => {

      await axios({
        method: 'get',
        url: `/user/${user_id}/full_profile`,
        headers: { 'Content-Type': 'application/json' },
      })
        .then(function (response) {
          const usersData = [response.data];
          users.value = usersData;
          console.log(usersData);
        })
        .catch(function (error) {
          console.error('Error fetching users:', error);
          // users.value = [];
        });
    };

    onMounted(() => {
      fetchData();
    });

    return {
      users,
      pdfContent,
      generatePDF
    };
  },
});
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

:root {
  --bg-sidebar: #18c29c;
  --light-green: #8ed7c6;
  --bg-color: #dce4e3;
  --light-grey: #dce4e3;
  --text-color: #084236;
}

body {
  background-color: var(--bg-color);
  height: 100vh;
  width: 100vw;
}

.sidebar {
  background-color: var(--bg-sidebar);
  position: fixed;
  height: 100%;
  width: 255px;
  transition: all .4s ease;
  white-space: nowrap;
  z-index: 1;
  margin-bottom: auto;
}

.sidebar.close {
  width: 78px;
  transition: all .4s ease;
}

header {
  display: flex;
  align-items: center;
  padding: 24px 29px;
  height: 80px;
  width: 100%;
}

header .logo-text {
  transition: all .4s ease;
}

header > img {
  position: absolute;
  right: 27px;
  cursor: pointer;
  transition: all .8s;
}

header > img.rotate {
  transition: all .3s linear;
  transform: rotate(-180deg);
}

.menu-links {
  width: 100%;
  list-style: none;
}

.menu-links a img {
  padding-left: 27px;
}

.menu-links > li {
  display: flex;
  align-items: center;
  background-color: var(--light-green);
  gap: 15px;
  margin: 0px 14px 20px;
  padding-left: 10px;
  height: 50px;
  border-radius: 12px;
  cursor: text;
  transition: all .2s ease;
}

.menu-links > li.change-bg {
  transition: all 1s linear;
  background-color: var(--light-grey);
}

.menu-links > li input {
  background-color: var(--light-green);
  outline: none;
  border: none;
  height: 100%;
  width: 100%;
  border-radius: 12px;
}

.dashboard-link span {
  transition: all .3s ease;
}

.courses-link span {
  transition: all .3s ease;
}

.fees-link span {
  transition: all .3s ease;
}

.certificate-link span {
  transition: all .3s ease;
}

.settings-link span {
  transition: all .3s ease;
}

.profile-link span {
  transition: all .3s ease;
}

.links-list a {
  display: flex;
  align-items: center;
  gap: 15px;
  width: 100%;
  height: 50px;
  margin-top: 10px;
  padding: 20px 0;
  text-decoration: none;
  color: var(--text-color);
  transition: all .4s ease;
  
}

.links-list a:hover {
  transition: all .4s ease;
  background-color: var(--light-green);
}

.bottom-content {
  display: flex;
  align-items: center;
  background-color: var(--light-green);
  position: absolute;
  gap: 9px;
  padding: 8px 14px;
  width: 100%;
  height: 60px;
  bottom: 0;
}

.bottom-content .user-image {
  display: flex;
  align-items: center;
  transition: all .3s linear
}

.bottom-content .user-image img {
  object-fit: cover;
  width: 45px;
  height: 45px;
  border-radius: 12px;
}

.bottom-content .user-data {
  display: flex;
  flex-direction: column;
  transition: all .3s linear
}

.user-data .user-name {
  font-size: 15px;
  font-weight: 400;
  color: var(--text-color);
}

.user-data .user-status {
  font-size: 12px;
  font-weight: 400;
  color: var(--text-color);
}

.bottom-content .logout {
  position: absolute;
  right: 27px;
  cursor: pointer;
}

.hideElement {
  opacity: 0;
  transition: all .3s linear;
}

section {
  background-color: var(--bg-color);
  position: absolute;
  top: 0;
  left: 255px;
  width: calc(100% -255px);
  transition: all .4s ease;
}

.sidebar.close ~ section {
  left: 78px;
  width: calc(100% -78px);
  transition: all .4s ease;
}

h1 {
  font-size: 25px;
  font-weight: 500;
  color: var(--text-color);
  padding: 18px;
}

p {
  font-size: 16px;
  font-weight: 500;
  color: var(--text-color);
  padding: 18px;
}
</style>