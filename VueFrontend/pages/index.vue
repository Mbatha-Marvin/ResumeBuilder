<template>
    <header>
        <nav>
            <ul>
                <li>
                    <NuxtLink to="/about">About</NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/posts">Posts</NuxtLink>
                </li>
            </ul>
        </nav>
    </header>
    <div>
        allow me to take such chance
    </div>
    <Footer />
</template>
  
  
<script setup>
const appConfig = useHead({
    title: 'ResumeBuilder',
    theme: {
        dark: true,
        colors: {
            primary: '#ff0000'
        }
    }
})

</script>
  