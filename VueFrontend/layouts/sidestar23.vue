<template>
  <div>
       <Sidebar />
       <section className='dashboard-contents'>
        <slot />
      </section>
    </div>

</template>

<script setup>
import Sidebar from "../components/userSidenav/Sidebar";



</script>

<style>

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
