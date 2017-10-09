import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    response: null
  },
  actions: {
    PostData: function ({commit}, data) {
	  var bodycontent = {
	   member:
		   {
			   first_name: data.firstName,
			   last_name: data.lastName,
			   id: data.id,
			   birth_date: data.birthDate
		   },
		   trading_partner_id: data.tradingPartnerId,
		   provider:
		   {		   
		       first_name: data.providerFirstName,
			   lastName: data.providerLastName,
			   npi: data.providerNpi
		   }
	  };
	  axios.post('http://localhost:5000/wt/api/v1.0/elegible', 
			bodycontent)
		  .then((response) => {
			commit('SET_RESPONSE', { result: response.data } )
		  }, (err) => {
			  console.log(err)
		  });
	}
  },
  mutations: {
	SET_RESPONSE: (state, { result } ) => {
		state.response = result	
	},
	SET_DELTE: (state, { text } ) => {
		state.textDelete = text	
	}
  },
  getters: {
    GET_RESPONSE: state => {
		return state.response
	}
  }
})
export default store