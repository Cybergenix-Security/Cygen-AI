from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML, CSS, and JavaScript combined
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Information Gathering Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #007bff;
        }
        input[type="text"] {
            width: 70%;
            padding: 10px;
            margin-bottom: 20px;
        }
        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .results {
            margin-top: 20px;
        }
        .category {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Information Gathering Tool</h1>
        <input type="text" id="domainInput" placeholder="Enter target domain" />
        <button id="gatherBtn">Gather Information</button>
        <div id="results" class="results"></div>
    </div>
    <script>
        document.getElementById('gatherBtn').addEventListener('click', function() {
            const domain = document.getElementById('domainInput').value;

            fetch('/gather', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ domain: domain })
            })
            .then(response => response.json())
            .then(data => {
                let resultsHTML = '<h2>Results:</h2>';
                
                resultsHTML += '<div class="category"><h3>Domain Information:</h3>';
                resultsHTML += `<p>Domain Name: ${data.domain_info.domain_name || 'N/A'}</p>`;
                resultsHTML += `<p>Registrar: ${data.domain_info.registrar || 'N/A'}</p>`;
                resultsHTML += `<p>Creation Date: ${data.domain_info.creation_date || 'N/A'}</p>`;
                resultsHTML += `<p>Expiration Date: ${data.domain_info.expiration_date || 'N/A'}</p></div>`;

                resultsHTML += '<div class="category"><h3>Website Content:</h3>';
                resultsHTML += `<p>${data.website_content || 'No content found.'}</p></div>`;

                resultsHTML += '<div class="category"><h3>Social Media Profiles:</h3>';
                resultsHTML += data.social_media_profiles.map(profile => `<p><a href="${profile}" target="_blank">${profile}</a></p>`).join('') || '<p>No profiles found.</p>';
                resultsHTML += '</div>';

                resultsHTML += '<div class="category"><h3>Publicly Available Documents:</h3>';
                resultsHTML += data.public_documents.join(', ') || 'No documents found.'; 
                resultsHTML += '</div>';

                resultsHTML += '<div class="category"><h3>Technical Information:</h3>';
                resultsHTML += `<p>${data.technical_info || 'No technical information found.'}</p></div>`;

                resultsHTML += '<div class="category"><h3>Third-Party Services:</h3>';
                resultsHTML += data.third_party_services.join(', ') || 'No third-party services found.'; 
                resultsHTML += '</div>';

                resultsHTML += '<div class="category"><h3>Email Addresses:</h3>';
                resultsHTML += data.email_addresses.join(', ') || 'No email addresses found.'; 
                resultsHTML += '</div>';

                resultsHTML += '<div class="category"><h3>News Articles and Blog Posts:</h3>';
                if (data.news_articles.length > 0) {
                    data.news_articles.forEach(article => {
                        resultsHTML += `<p><a href="${article.url}" target="_blank">${article.title}</a></p>`;
                    });
                } else {
                    resultsHTML += '<p>No news articles found.</p>';
                }
                resultsHTML += '</div>';

                resultsHTML += '<div class="category"><h3>Competitor Insights:</h3>';
                resultsHTML += data.competitor_insights.join(', ') || 'No insights found.'; 
                resultsHTML += '</div>';

                resultsHTML += '<div class="category"><h3>Online Reviews:</h3>';
                resultsHTML += data.online_reviews.join(', ') || 'No reviews found.'; 
                resultsHTML += '</div>';

                resultsHTML += '<div class="category"><h3>Data Breaches:</h3>';
                if (data.breaches.length > 0) {
                    data.breaches.forEach(breach => {
                        resultsHTML += `<p>${breach.Name}: ${breach.BreachDate}</p>`;
                    });
                } else {
                    resultsHTML += '<p>No data breaches found.</p>';
                }
                resultsHTML += '</div>';

                resultsHTML += '<div class="category"><h3>API Endpoints:</h3>';
                resultsHTML += data.api_endpoints.join(', ') || 'No API endpoints found.'; 
                resultsHTML += '</div>';

                resultsHTML += '<div class="category"><h3>Security Headers:</h3>';
                resultsHTML += `<p>${data.security_headers || 'No security headers found.'}</p></div>`;
                
                document.getElementById('results').innerHTML = resultsHTML;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
'''

# Route for the index page
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

# Route to gather information
@app.route('/gather', methods=['POST'])
def gather():
    domain = request.json['domain']
    
    # Dummy data for demonstration; replace with actual data gathering logic
    info = {
        'domain_info': {
            'domain_name': domain,
            'registrar': 'Example Registrar',
            'creation_date': 'Example Date',
            'expiration_date': 'Example Date',
        },
        'website_content': 'Headings: CYBERGENIX, WELCOME<br>Links: <a href="https://www.cybergenixsecurity.com/about-6">About Us</a>, <a href="https://www.cybergenixsecurity.com/services-9">Services</a>',
        'social_media_profiles': [
            'https://www.facebook.com/example',
            'https://twitter.com/example',
            'https://www.linkedin.com/company/example'
        ],
        'public_documents': ['Privacy Policy', 'Terms of Service'],
        'technical_info': 'Hosting Provider: Example Host<br>IP Address: 192.168.1.1',
        'third_party_services': ['Google Analytics', 'Facebook Pixel'],
        'email_addresses': ['contact@example.com', 'support@example.com'],
        'news_articles': [{'title': 'Sample Article', 'url': 'https://example.com'}],
        'competitor_insights': ['Competitor A', 'Competitor B'],
        'online_reviews': ['TrustPilot: 4.5 stars'],
        'breaches': [],
        'api_endpoints': ['GET /api/data', 'POST /api/data'],
        'security_headers': 'Strict-Transport-Security: max-age=86400'
    }
    
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
