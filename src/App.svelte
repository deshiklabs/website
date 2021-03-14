<script>
	import {Route,router} from 'tinro';
import Footer from "./components/footer.svelte";
import Nav from "./components/nav.svelte";
import Home from "./pages/home.svelte";
import About from "./pages/about.svelte";
import Contact from "./pages/contact.svelte";
import Products from "./pages/products.svelte";
import Services from "./pages/services.svelte";
import Careers from "./pages/careers.svelte";

router.mode.hash();
</script>

<style lang="scss" global>
	@charset "utf-8";
	
	$primary: hsl(204, 86%, 53%);
	
	@import "bulma/bulma.sass";
</style>

<main>
	<Nav/>
	
	<Route path="/"><Home/></Route>
	<Route path="/about"><About/></Route>
	<Route path="/contact"><Contact/></Route>
	<Route path="/careers"><Careers/></Route>
	<Route path="/services"><Services/></Route>
	<Route path="/products"><Products/></Route>

	<Footer/>
</main>