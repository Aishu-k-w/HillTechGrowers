// Main JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Water flow control functionality
    const startBtn = document.getElementById('start-btn');
    const stopBtn = document.getElementById('stop-btn');
    const flowStatus = document.getElementById('flow-status');

    if (startBtn && stopBtn && flowStatus) {
        let isFlowActive = false;

        startBtn.addEventListener('click', function() {
            isFlowActive = true;
            updateFlowStatus();

            // Send API request
            fetch('/api/water_control', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ action: 'start' })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Water flow started:', data);
            })
            .catch(error => {
                console.error('Error:', error);
                isFlowActive = false;
                updateFlowStatus();
            });
        });

        stopBtn.addEventListener('click', function() {
            isFlowActive = false;
            updateFlowStatus();

            // Send API request
            fetch('/api/water_control', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ action: 'stop' })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Water flow stopped:', data);
            })
            .catch(error => {
                console.error('Error:', error);
                isFlowActive = true;
                updateFlowStatus();
            });
        });

        function updateFlowStatus() {
            if (isFlowActive) {
                flowStatus.textContent = 'ACTIVE';
                flowStatus.className = 'status-indicator status-active';
                startBtn.disabled = true;
                stopBtn.disabled = false;
            } else {
                flowStatus.textContent = 'STOPPED';
                flowStatus.className = 'status-indicator status-stopped';
                startBtn.disabled = false;
                stopBtn.disabled = true;
            }
        }
    }

    // Auto-refresh data every 30 seconds
    if (window.location.pathname === '/dashboard') {
        setInterval(function() {
            // In a real application, you would fetch updated data here
            console.log('Auto-refreshing dashboard data...');
        }, 30000);
    }

    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading states to buttons
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', function() {
            if (!this.disabled) {
                this.style.opacity = '0.7';
                setTimeout(() => {
                    this.style.opacity = '1';
                }, 300);
            }
        });
    });
});

// Utility functions
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;

    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: white;
        font-weight: 600;
        z-index: 1000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;

    if (type === 'success') {
        notification.style.background = '#16a34a';
    } else if (type === 'error') {
        notification.style.background = '#dc2626';
    } else if (type === 'warning') {
        notification.style.background = '#f97316';
    } else {
        notification.style.background = '#2563eb';
    }

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);

    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Format numbers with appropriate units
function formatValue(value, unit) {
    if (typeof value === 'number') {
        return value.toFixed(1) + unit;
    }
    return value + unit;
}

// Update timestamp display
function updateTimestamp() {
    const timestampElements = document.querySelectorAll('.timestamp');
    const now = new Date();
    const timeString = now.toLocaleString();

    timestampElements.forEach(element => {
        element.textContent = timeString;
    });
}

// Initialize timestamp updates
if (document.querySelector('.timestamp')) {
    updateTimestamp();
    setInterval(updateTimestamp, 1000);
}