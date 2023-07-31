<template>
    <div class="container footer-padding">
        <div class="footer">
            <blockquote class="blockquote mb-2">
                <p>Designed by</p>
                <footer class="blockquote-footer">
                    <NuxtLink>Daring Coders</NuxtLink>
                </footer>
            </blockquote>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    color: white;
    text-align: center;
    background-color: #053116;
    background-image: linear-gradient(to right, #064928, indigo);
}

.footer-padding {
    margin-top: 20px;
}
</style>