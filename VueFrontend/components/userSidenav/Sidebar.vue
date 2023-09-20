<template>
    <nav class="sidebar">

      <SidebarHeader />

        <div class="menu-links">
            <li class="search-box">
                <img :src="search" alt="search-image">
                <input type="search" placeholder="Search">
            </li>

            <ul class="links-list">
              <li v-for="(item, index) in sidebardata" :key="index" :class="item.className">
                <NuxtLink :to="item.path">
                  <img class="icon" :src="item.icon" alt="dashboard" />
                  <span :class="`${item.className} span`">{{ item.title }}</span>
                </NuxtLink>
              </li>
            </ul>
        </div>
        
        <div v-for="(user, index) in userdata" :key="index" class="bottom-content">
            <div :class="`user-image`">
              <img :src="user.icon" alt="user-image" />
            </div>
            <div :class="user.className">
              <span class="user-name">{{ user.userName }}</span>
              <span class="user-status">{{ user.course }}</span>
            </div>
            <img class="logout" :src="logout" alt="logout" />
          </div>
            
    </nav>
</template>

<script setup>
const sidebardata = useNuxtApp().$sidebardata;
const userdata = useNuxtApp().$userdata;
import logout from '../../assets/userNavigation/icons/log-out.svg';
import search from '../../assets/userNavigation/icons/search.svg';
import SidebarHeader from './SidebarHeader';

</script>

<style>

</style>