<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Publications | InterphasesTeam</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Montserrat:wght@700&display=swap" rel="stylesheet">
    <style>
        /* Reuse core styles */
        :root { --bg: #ffffff; --text: #1a1a1a; --accent: #0070f3; --secondary: #666; }
        body { font-family: 'Inter', sans-serif; margin: 0; color: var(--text); }
        
        nav { display: flex; justify-content: space-between; align-items: center; padding: 20px 5%; background: white; border-bottom: 1px solid #eee; position: sticky; top: 0; z-index: 1000; }
        .logo { font-family: 'Montserrat', sans-serif; font-size: 1.5rem; color: var(--text); text-decoration: none; }
        .nav-links { display: flex; gap: 25px; }
        .nav-links a { text-decoration: none; color: var(--text); font-weight: 500; }

        .container { max-width: 800px; margin: 60px auto; padding: 0 20px; }

        /* --- PUBLICATIONS STYLES --- */
        .year-section { margin-top: 40px; }
        .year-label { 
            font-size: 1.5rem; 
            color: var(--accent); 
            border-bottom: 2px solid #eee; 
            padding-bottom: 5px; 
            margin-bottom: 20px; 
        }

        .pub-item {
            margin-bottom: 25px;
            padding-left: 15px;
            border-left: 3px solid #eee;
        }

        .pub-title { font-weight: 600; display: block; font-size: 1.1rem; margin-bottom: 5px; }
        .pub-authors { color: var(--secondary); font-size: 0.95rem; }
        .pub-journal { font-style: italic; color: #444; }
        .pub-links { margin-top: 8px; font-size: 0.85rem; }
        .pub-links a { color: var(--accent); text-decoration: none; margin-right: 15px; font-weight: 600; }
    </style>
</head>
<body>

    <nav>
        <a href="index.html" class="logo">InterphasesTeam</a>
        <div class="nav-links">
            <a href="research.html">Research</a>
            <a href="team.html">Team</a>
            <a href="publications.html">Publications</a>
            <a href="contact.html">Contact</a>
        </div>
    </nav>

    <div class="container">
        <h1>Selected Publications</h1>

        <div class="year-section">
            <div class="year-label">2026</div>
            
            <div class="pub-item">
                <span class="pub-title">Neural Interphase Dynamics in Synthetic Environments</span>
                <span class="pub-authors">Rivera, A., Chen, S., & Smyth, J.</span><br>
                <span class="pub-journal">Nature Materials, 12(4), 450-462.</span>
                <div class="pub-links">
                    <a href="#">DOI Link</a>
                    <a href="#">Download PDF</a>
                </div>
            </div>
        </div>

        <div class="year-section">
            <div class="year-label">2025</div>
            
            <div class="pub-item">
                <span class="pub-title">A New Approach to Molecular Stability</span>
                <span class="pub-authors">Chen, S. & Rivera, A.</span><br>
                <span class="pub-journal">Journal of Applied Physics, 118(2), 101-115.</span>
                <div class="pub-links">
                    <a href="#">DOI Link</a>
                </div>
            </div>
        </div>
    </div>

</body>
</html>