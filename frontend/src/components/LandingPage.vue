<template>
  <div class="landing-page">
    <HeroComponent />
    <div class="content">
      <!-- Additional content sections styled in DENSO's clean, minimal aesthetic -->
      <section class="section">
        <h2>Our Innovation</h2>
        <p>DENSO is dedicated to leading the way in automotive technology and sustainable design.</p>
      </section>
      <section class="section">
        <h2>Quality & Reliability</h2>
        <p>With over 42,000 patents, every product is engineered to the highest standards.</p>
      </section>
    </div>
  </div>
</template>

<script>
import HeroComponent from '@/components/HeroComponent.vue'

export default {
  name: 'LandingPage',
  components: {
    HeroComponent
  }
}
</script>

<style scoped>
.landing-page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.content {
  flex: 1;
  padding: 40px;
  background-color: #fff;
  font-family: Arial, sans-serif;
}
.section {
  margin-bottom: 40px;
}
.section h2 {
  color: #e60012;
  font-size: 32px;
  margin-bottom: 10px;
  font-family: 'DENSO Sans', sans-serif;
}
.section p {
  color: #333;
  font-size: 18px;
}
</style>
