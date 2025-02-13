<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="robots" content="noindex, nofollow">
    <title>${msg("loginTitle")}</title>
    <link rel="icon" type="image/x-icon" href="${url.resourcesPath}/img/favicon.ico" />
    <link href="${url.resourcesPath}/css/styles.css" rel="stylesheet" />
</head>
<body>
    <div class="login-container">
        <div class="login-card">
            <div class="login-header">
                <img src="${url.resourcesPath}/img/denso-logo.png" alt="DENSO Logo" class="logo" />
                <h1>Welcome to DENSO</h1>
                <p>Sign in to access your account</p>
            </div>
            <form id="kc-form-login" action="${url.loginAction}" method="post">
                <div class="form-group">
                    <label for="username">${msg("usernameOrEmail")}</label>
                    <input type="text" id="username" name="username" class="form-control" placeholder="Enter your username or email" required />
                </div>
                <div class="form-group">
                    <label for="password">${msg("password")}</label>
                    <div class="password-wrapper">
                        <input type="password" id="password" name="password" class="form-control" placeholder="Enter your password" required />
                        <button type="button" class="reveal-password" onclick="togglePasswordVisibility()">
                            <span class="eye-icon">👁️</span> <!-- Use an icon or text -->
                        </button>
                    </div>
                </div>
                <div class="form-group">
                    <button type="submit" class="btn btn-primary">${msg("doLogIn")}</button>
                </div>
            </form>
            <div class="login-footer">
                <p>© 2025 DENSO Corporation. All rights reserved.</p>
            </div>
        </div>
    </div>
    <script>
        function togglePasswordVisibility() {
            const passwordInput = document.getElementById('password');
            const eyeIcon = document.querySelector('.eye-icon');
    
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                eyeIcon.textContent = '👁️'; // Change icon/text when password is visible
            } else {
                passwordInput.type = 'password';
                eyeIcon.textContent = '👁️'; // Change icon/text when password is hidden
            }
        }
    </script>
</body>
</html>