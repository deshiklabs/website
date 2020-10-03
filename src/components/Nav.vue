  <template>
  <div class="center examplex">
    <vs-navbar center-collapsed>
      <template #left>
        <img src="@/assets/logo-wide.png" alt="" style="height: 28px" />
      </template>
      <vs-navbar-item to="/">
        Home
      </vs-navbar-item>
      <vs-navbar-item to="/about">
        About
      </vs-navbar-item>
      <vs-navbar-item>
        Software
      </vs-navbar-item>
      <vs-navbar-item>
        3D Printing
      </vs-navbar-item>
      <template #right>
        <vs-button circle>Contact </vs-button>
      </template>
    </vs-navbar>
  </div>
</template>

  <script>
export default {
  name: "Nav",
  data: () => ({
  }),
};
</script>