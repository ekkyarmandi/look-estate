<template>
  <div class="wrapper">
    <footer>
      <div class="content">
        <Logo />
        <div class="contact">
          <p class="label">Contact</p>
          <div>
            <MailIcon />
            <a class="email" href="mailto:ekkyarmandi.com">ekkyarmandi@gmail.com</a>
          </div>
          <div>
            <PhoneIcon />
            <p>+62 899 9999 9999</p>
          </div>
        </div>
      </div>
      <div class="links">
        <div>
          <p class="label">Contact</p>
          <ul>
            <li><a href="#">Bali</a></li>
            <li><a href="#">Yogyakarta</a></li>
            <li><a href="#">Bandung</a></li>
            <li><a href="#">Jakarta</a></li>
          </ul>
        </div>
        <div>
          <p class="label">Information</p>
          <ul>
            <li><a href="#">Blog</a></li>
            <li><a href="#">Testimonials</a></li>
            <li><a href="#">About Us</a></li>
          </ul>
        </div>
        <div>
          <p class="label">Follow Us</p>
          <ul>
            <li><a href="#">Facebook</a></li>
            <li><a href="#">Twitter</a></li>
            <li><a href="#">Instagram</a></li>
            <li><a href="#">Pinterest</a></li>
          </ul>
        </div>
      </div>
    </footer>
    <p class="copyright">&copy; Copyright 2024. <a href="https://ekkyarmandi.com">EkkyArmandi.com</a>. All Rights Reserved.</p>
  </div>
</template>

<script setup>
import Logo from "@/assets/icons/Logo.vue";
import MailIcon from "@/assets/icons/MailIcon.vue";
import PhoneIcon from "@/assets/icons/PhoneIcon.vue";
</script>

<style scoped>
a,
p {
  color: white;
  text-decoration: none;
}
a:hover {
  color: var(--primary-500);
  text-decoration: underline;
}
footer {
  display: flex;
  justify-content: space-between;
  padding: 60px 0 28px 0;
  border-bottom: 1px solid #ccc;
}
p.copyright {
  padding: 12px 0;
}
p.copyright a {
  color: var(--primary-500);
}
/* links */
@media only screen and (min-width: 600px) {
  footer {
    padding: 40px 0 28px 0;
  }
  .links {
    display: flex;
    gap: 4rem;
  }
}
@media only screen and (min-width: 992px) {
  .links {
    display: flex;
    gap: 5rem;
  }
}
ul {
  display: flex;
  flex-direction: column;
  gap: 8px;
  list-style-type: none;
}
p.label {
  margin-bottom: 1rem;
  font-weight: 700;
}
.content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.contact {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.contact div {
  display: flex;
  gap: 8px;
}
</style>
