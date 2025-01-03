import React, { Component } from 'react';
import $ from 'jquery';

import '../stylesheets/FormView.css';

class FormView extends Component {
	constructor(props){
		super();
		this.state = {
			title: "",
			author: "",
			rating: 1,
			search: '',
		}
	}

	submitBook = (event) => {
		event.preventDefault();
		$.ajax({
			url: '/books', //TODO: update request URL
			type: "POST",
			dataType: 'json',
			contentType: 'application/json',
			data:JSON.stringify({
				title: this.state.title,
				author: this.state.author,
				rating: this.state.rating
			}),
			xhrFields: {
				withCredentials: true
			},
			crossDomain: true,
			success: (result) => {
				document.getElementById("add-book-form").reset();
				return;
			},
			error: (error) => {
				alert('Unable to add book. Please try your request again')
				return;
			}
		})
	}

	handleSearch = (event) => {
		event.preventDefault();
		this.props.searchBooks(this.state.search);
	}

	handleChange = (event) => {
		this.setState({[event.target.name]:event.target.value})
	}
