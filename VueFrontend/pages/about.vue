<template>
  <div class="page-wrapper">
    <div class="button-wrapper prev-button-wrapper">
      <button class="prev-button" @click="goToPrevious">Previous</button>
    </div>
    <div class="button-wrapper next-button-wrapper">
      <button class="next-button" @click="goToNext">Next</button>
    </div>
    <div class="container">
      <div class="card border-light">
        <!-- <div class="card-header">
          Quote
        </div> -->
        <div class="card-body">
          <blockquote class="blockquote mb-0">
            <p>Welcome to Resume Builder Home page.</p>
            <footer class="blockquote-footer">Find more</footer>
          </blockquote>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToPrevious() {
      // Implement logic to navigate to the previous quote
    },
    goToNext() {
      // Implement logic to navigate to the next quote
    },
  },
};
</script>

<style>
html,
body,
.page-wrapper {
  height: 100%;
  margin: 0;
  padding: 0;
}

.page-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
}

.container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card {
  /* Add your desired styles for the card here */
  /* border: #0026ff !important; */
  border-radius: 4px !important;  
}

.button-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  width: 100%;
  top: 0;
  bottom: 0;
}

.prev-button-wrapper {
  left: 0;
}

.next-button-wrapper {
  right: 0;
}

.prev-button,
.next-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

/* Additional styles to make the buttons visible on hover */
.prev-button:hover,
.next-button:hover {
  background-color: #0056b3;
}
</style>
