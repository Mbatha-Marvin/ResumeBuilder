<template>
    <p>Post id {{ route.params.id }}</p>
</template>

<script setup>
const route = useRoute()

// When accessing /posts/1, route.params.id will be 1
console.log(route.params.id)
</script>
