<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
		<div class="columns medium-3">
			<h2>Member data</h2>
			    <p>First Name: <input v-model="firstName"></p>
				<p>Last Name: <input v-model="lastName"></p>
				<p>Insurance Id: <input v-model="id"></p>
				<p>Birth Date: <input type="date" v-model="birthDate"></p>
		</div>
		<div class="columns medium-3">
			<h2>Provider data</h2>
				<p>First Name: <input v-model="providerFirstName"></p>
				<p>Last Name: <input v-model="providerLastName"></p>
				<p>NPI: <input v-model="providerNpi"></p>	
		</div>
		<div class="columns medium-3">
			<h2>Traiding Partner data</h2>
				<p>Id: <input v-model="tradingPartnerId"></p>
		</div>
	<button v-on:click="methodSubmit">SUBMIT</button>
	<div>
		<h2>Pokitdok response</h2>
		<p>{{response}}</p>
	</div>
	
  </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
  name: 'CustomCli',
  computed : mapState([
	'response',
	'textDelete'
  ]),
  http: {
    emulateJSON: true,
	emulateHTTP: true
  },
  data () {
    return {
      msg: 'Pokitdok client',
	  firstName: 'Jane',
	  lastName: 'Doe',
	  id: 'AN_INSURANCE_ID',
	  birthDate: '2017-07-04',
	  tradingPartnerId: 'insurance_name',
	  providerFirstName: 'Alan',
	  providerLastName: 'Greence',
	  providerNpi: '1295128288',
    }
  },
  methods: {
    methodSubmit() {
		this.$store.dispatch('PostData',this._data)
	}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
