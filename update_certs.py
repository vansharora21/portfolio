import codecs
import re

content = codecs.open("c:\\Users\\BIT\\Desktop\\VS CODE WORKSPACE\\MY WORK\\portfolio\\personal portfolio vansh\\index.html", "r", "utf-8").read()

start_marker = '<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">'
end_marker = '</section>'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_html = """<!-- Premium Certificates Carousel -->
      <div class="swiper certificate-swiper position-relative pb-5" data-aos="fade-up" data-aos-delay="200">
        <div class="swiper-wrapper">
          
          <!-- Canva -->
          <div class="swiper-slide">
            <a href="images/certificates/canva.png" data-lightbox="certificates" data-title="Canva Design" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/canva.png" class="certificate-img" alt="Canva Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">Canva Design</h5>
                  <span class="text-white-50 small"><i class="fas fa-search-plus"></i> View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- C/C++ -->
          <div class="swiper-slide">
            <a href="images/certificates/cc++.png" data-lightbox="certificates" data-title="C/C++ Programming" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/cc++.png" class="certificate-img" alt="C/C++ Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">C/C++ Programming</h5>
                  <span class="text-white-50 small"><i class="fas fa-search-plus"></i> View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- Chatbot -->
          <div class="swiper-slide">
            <a href="images/certificates/chatbot.png" data-lightbox="certificates" data-title="Chatbot Development" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/chatbot.png" class="certificate-img" alt="Chatbot Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">Chatbot Development</h5>
                  <span class="text-white-50 small">View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- Frontend -->
          <div class="swiper-slide">
             <a href="images/certificates/frontend.png" data-lightbox="certificates" data-title="Frontend Web Development" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/frontend.png" class="certificate-img" alt="Frontend Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">Frontend Web Dev</h5>
                  <span class="text-white-50 small">View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- Full Stack -->
          <div class="swiper-slide">
             <a href="images/certificates/full stack.png" data-lightbox="certificates" data-title="Full Stack Web Development" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/full stack.png" class="certificate-img" alt="Full Stack Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">Full Stack Web Dev</h5>
                  <span class="text-white-50 small">View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- Mastery in JS -->
          <div class="swiper-slide">
             <a href="images/certificates/mastery in js.png" data-lightbox="certificates" data-title="Mastery in JavaScript" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/mastery in js.png" class="certificate-img" alt="JavaScript Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">Mastery in JS</h5>
                  <span class="text-white-50 small">View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- Matplotlib -->
          <div class="swiper-slide">
             <a href="images/certificates/matplotlib.png" data-lightbox="certificates" data-title="Matplotlib Library" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/matplotlib.png" class="certificate-img" alt="Matplotlib Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">Matplotlib Library</h5>
                  <span class="text-white-50 small">View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- Python PDF Lib -->
          <div class="swiper-slide">
             <a href="images/certificates/python pdf lib.png" data-lightbox="certificates" data-title="Python Libraries" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/python pdf lib.png" class="certificate-img" alt="Python Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">Python Libraries</h5>
                  <span class="text-white-50 small">View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- React -->
          <div class="swiper-slide">
             <a href="images/certificates/react.png" data-lightbox="certificates" data-title="React.js Framework" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/react.png" class="certificate-img" alt="React Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">React.js Framework</h5>
                  <span class="text-white-50 small">View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- SQL -->
          <div class="swiper-slide">
             <a href="images/certificates/sql.png" data-lightbox="certificates" data-title="SQL Database Management" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/sql.png" class="certificate-img" alt="SQL Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">SQL Database Mgmt</h5>
                  <span class="text-white-50 small">View Certificate</span>
                </div>
              </div>
            </a>
          </div>

          <!-- UI/UX -->
          <div class="swiper-slide">
             <a href="images/certificates/ui ux.png" data-lightbox="certificates" data-title="UI/UX Design" class="text-decoration-none">
              <div class="certificate-card rounded-4 overflow-hidden position-relative">
                <img src="images/certificates/ui ux.png" class="certificate-img" alt="UI/UX Certificate">
                <div class="certificate-overlay">
                  <h5 class="text-white fw-bold text-center mb-1">UI/UX Design</h5>
                  <span class="text-white-50 small">View Certificate</span>
                </div>
              </div>
            </a>
          </div>

        </div>
        
        <!-- Pagination -->
        <div class="swiper-pagination mt-4 position-relative"></div>
      </div>
    
"""
    content = content[:start_idx] + new_html + content[end_idx:]
    codecs.open("c:\\Users\\BIT\\Desktop\\VS CODE WORKSPACE\\MY WORK\\portfolio\\personal portfolio vansh\\index.html", "w", "utf-8").write(content)
    print("Successfully replaced certificates section")
