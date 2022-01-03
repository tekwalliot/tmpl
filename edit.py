<!DOCTYPE html>
{% load static %} 
<html>
	<head>
<!-- 		<meta charset="utf-8" /> -->
<!-- 		<title>A simple, clean, and responsive HTML invoice template</title> -->

		<style>
			.invoice-box {
				max-width: 900px;
				margin: auto;
				padding: 10px 20px 20px 20px;
				border: 2px solid green;
                        border-radius: 10px;
				box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
				font-size: 16px;
				line-height: 24px;
				font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
				color: #555;
			}

			.invoice-box table {
				width: 100%;
				line-height: inherit;
				text-align: left;
			}

			.invoice-box table td {
				padding: 5px;
				vertical-align: top;
			}

			.invoice-box table tr td:nth-child(2) {
				text-align: right;
			}

			.invoice-box table tr.top table td {
				padding-bottom: 20px;
			}

			.invoice-box table tr.top table td.title {
				font-size: 45px;
				line-height: 45px;
				color: #333;
			}

			.invoice-box table tr.information table td {
				padding-bottom: 40px;
			}

			.invoice-box table tr.heading td {
				background: #eee;
				border-bottom: 1px solid #ddd;
				font-weight: bold;
			}

			.invoice-box table tr.details td {
				padding-bottom: 20px;
			}

			.invoice-box table tr.item td {
				border-bottom: 1px solid #eee;
			}

			.invoice-box table tr.item.last td {
				border-bottom: none;
			}

			.invoice-box table tr.total td:nth-child(2) {
				border-top: 2px solid #eee;
				font-weight: bold;
			}

			@media only screen and (max-width: 600px) {
				.invoice-box table tr.top table td {
					width: 100%;
					display: block;
					text-align: center;
				}

				.invoice-box table tr.information table td {
					width: 100%;
					display: block;
					text-align: center;
				}
			}

			/** RTL **/
			.invoice-box.rtl {
				direction: rtl;
				font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
			}

			.invoice-box.rtl table {
				text-align: right;
			}

			.invoice-box.rtl table tr td:nth-child(2) {
				text-align: left;
			}
		</style>
	</head>

	<body>
		<div class="invoice-box">


    <img style="width: 100%;float: left; max-width: 120px" src="{% static 'img/siva.png' %}">
   <img style="width: 100%; float: right; height:110px; max-width: 110px" src="{% static 'img/hanuman.png' %}">
     <h3 style="text-align:center; color: #850101">SRI SRI PARVATHAVARTHANI SAMETHA RAMALINGSWARA SWAMY SAHITHA SRI ABHAYA ANJANEYA SWAMY DEVALAYAM <br><a style="font-size: 13px; color:orange">Srinivasa Colony, Beside Aditya Nagar, Hydernagar, Hyderabad-90</a></h3>
     <br>

<h3 style="text-align: center; margin-top: -15px; color: #0000A5">RECEIPT</h3>



			<table cellpadding="0" cellspacing="0">
				<tr class="top">
					<td colspan="2">
						<table>
							<tr>
								<td style="color: green; font-size: 17px; font-weight: bold">
									Receipt No: 25365 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mobile No: 9440370989
								</td>

								<td>
									Date: 23 Dec 2021<br />
								</td>
							</tr>
						</table>
					</td>
				</tr>

                        <tr class="details">
                              <td style="font-style: italic; color: orange">Received with thanks from</td>
                              <td style="font-weight: bold; color: #0000A5">Category: Gothranamalu Yearly</td>
                        </tr>
				<tr class="heading">
					<td>Name</td>

					<td>Sri NCHV Laxmanacharyulu</td>
				</tr>

				<tr class="details">
					<td>Gothram</td>

					<td>Kousikasa</td>
				</tr>

				<tr class="heading">
					<td>Towards Gothranamalu Yearly</td>

					<td>Amount</td>
				</tr>

				<tr class="item">
					<td>Paid through Online</td>

					<td style="font-weight: bold; color: black; font-size: 20px;">₹ 2500 /-</td>
				</tr>

                        <tr class="item">
                              <td style="font-size: 14px; font-style: italic;">Authorised Digital Receipt</td>
                              <td style="font-size: 14px; font-style: italic;">Issued By Subba Raju Garu</td>
                        </tr>
			</table>
                  <h4 style="text-align: center; font-weight: normal; margin-bottom: 0px; background: #800080; padding:5px 5px; border-radius: 5px; color: white">రూ 2500 /-  &nbsp;చెల్లించి సంవత్సరకాలం పాటు   నిత్య గోత్రనామాల పూజ
చేయించుకోగలరు</h4>
		</div>

	</body>
</html>