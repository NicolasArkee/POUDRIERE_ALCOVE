import streamlit as st
import subprocess
import os
import tempfile
from pathlib import Path

st.set_page_config(
    page_title="Video Masker pour Alcôve",
    page_icon="🎭",
    layout="wide"
)

st.title("🎭 Video Masker & Ratio Standardizer")
st.write("Transformez vos vidéos en 16:9 avec un masque personnalisé pour projection en alcôve.")

# --- BARRE LATÉRALE : CONFIGURATION ---
st.sidebar.header("⚙️ Paramètres de conversion")

# Résolution
target_res_options = {
    "Full HD (1920x1080)": "1920:1080",
    "HD (1280x720)": "1280:720",
    "4K (3840x2160)": "3840:2160"
}
selected_res = st.sidebar.selectbox(
    "Résolution de sortie",
    options=list(target_res_options.keys()),
    index=0
)
target_res = target_res_options[selected_res]

# Qualité
crf_value = st.sidebar.slider(
    "Qualité vidéo (CRF)",
    min_value=15,
    max_value=28,
    value=18,
    help="Plus bas = meilleure qualité (mais fichier plus lourd). Recommandé: 18-23"
)

# Préréglages d'encodage
preset_options = ["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"]
preset_value = st.sidebar.selectbox(
    "Vitesse d'encodage",
    options=preset_options,
    index=4,
    help="'fast' est un bon compromis. 'slow' donne une meilleure qualité mais prend plus de temps."
)

st.sidebar.markdown("---")
st.sidebar.info("""
**ℹ️ Comment ça marche ?**

1. Uploadez votre vidéo (n'importe quel ratio)
2. Uploadez un masque PNG 16:9 avec transparence
3. L'outil va:
   - Redimensionner la vidéo en 16:9
   - Ajouter des bandes noires si nécessaire
   - Appliquer le masque par-dessus
""")

# --- ZONE D'UPLOAD ---
st.markdown("### 📤 Étape 1 : Chargez vos fichiers")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Vidéo source")
    uploaded_video = st.file_uploader(
        "Choisissez une vidéo...",
        type=["mp4", "mov", "avi", "mkv", "webm"],
        help="Formats supportés: MP4, MOV, AVI, MKV, WebM"
    )

    if uploaded_video:
        st.success(f"✅ Vidéo chargée: {uploaded_video.name}")
        file_size_mb = uploaded_video.size / (1024 * 1024)
        st.caption(f"Taille: {file_size_mb:.2f} MB")

with col2:
    st.markdown("#### Masque PNG")
    uploaded_mask = st.file_uploader(
        "Choisissez votre masque PNG (16:9 avec transparence)",
        type=["png"],
        help="Le masque doit être en 16:9 avec canal alpha (transparence)"
    )

    if uploaded_mask:
        st.success(f"✅ Masque chargé: {uploaded_mask.name}")
        st.image(uploaded_mask, caption="Aperçu du masque", use_container_width=True)

# --- TRAITEMENT ---
if uploaded_video and uploaded_mask:
    st.markdown("---")
    st.markdown("### 🎬 Étape 2 : Lancer le traitement")

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

    with col_btn2:
        process_button = st.button(
            "🚀 Lancer le rendu de la vidéo",
            use_container_width=True,
            type="primary"
        )

    if process_button:
        progress_bar = st.progress(0)
        status_text = st.empty()

        try:
            # Création de fichiers temporaires
            status_text.text("📥 Préparation des fichiers...")
            progress_bar.progress(10)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as t_video:
                t_video.write(uploaded_video.read())
                t_video_path = t_video.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as t_mask:
                t_mask.write(uploaded_mask.read())
                t_mask_path = t_mask.name

            progress_bar.progress(20)

            # Nom du fichier de sortie
            output_filename = "video_masquee_16-9.mp4"

            # Construction de la commande FFmpeg
            status_text.text("🎨 Application du masque et conversion du ratio...")
            progress_bar.progress(30)

            # Commande FFmpeg optimisée
            # [0:v] gère le redimensionnement et le padding (bandes noires si pas 16:9)
            # [1:v] applique le masque par dessus
            cmd = [
                'ffmpeg', '-y',
                '-i', t_video_path,
                '-i', t_mask_path,
                '-filter_complex',
                f"[0:v]scale={target_res}:force_original_aspect_ratio=decrease,pad={target_res}:(ow-iw)/2:(oh-ih)/2[bg];"
                "[bg][1:v]overlay=0:0[out]",
                '-map', '[out]',
                '-map', '0:a?',  # Copie l'audio si présent
                '-c:v', 'libx264',
                '-crf', str(crf_value),
                '-preset', preset_value,
                '-c:a', 'aac',  # Codec audio
                '-b:a', '192k',  # Bitrate audio
                output_filename
            ]

            progress_bar.progress(40)

            # Exécution de FFmpeg
            with st.spinner("⏳ FFmpeg traite la vidéo... Cela peut prendre quelques minutes selon la taille."):
                process = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    check=True
                )

            progress_bar.progress(90)
            status_text.text("✨ Finalisation...")

            # Vérification que le fichier existe
            if os.path.exists(output_filename) and os.path.getsize(output_filename) > 0:
                progress_bar.progress(100)
                status_text.text("✅ Traitement terminé avec succès!")

                st.markdown("---")
                st.markdown("### 🎉 Résultat")

                # Affichage de la vidéo
                st.video(output_filename)

                # Statistiques du fichier
                output_size_mb = os.path.getsize(output_filename) / (1024 * 1024)
                col_stats1, col_stats2, col_stats3 = st.columns(3)
                with col_stats1:
                    st.metric("Résolution", selected_res)
                with col_stats2:
                    st.metric("Taille du fichier", f"{output_size_mb:.2f} MB")
                with col_stats3:
                    st.metric("Qualité (CRF)", crf_value)

                # Bouton de téléchargement
                with open(output_filename, "rb") as file:
                    st.download_button(
                        label="⬇️ Télécharger la vidéo finale",
                        data=file,
                        file_name=f"video_alcove_{Path(uploaded_video.name).stem}.mp4",
                        mime="video/mp4",
                        use_container_width=True,
                        type="primary"
                    )

                st.success("🎊 Votre vidéo est prête pour la projection en alcôve!")
            else:
                st.error("❌ Erreur: Le fichier de sortie n'a pas été créé correctement.")

            # Nettoyage des fichiers temporaires
            try:
                os.remove(t_video_path)
                os.remove(t_mask_path)
            except:
                pass

        except subprocess.CalledProcessError as e:
            progress_bar.empty()
            status_text.empty()
            st.error("❌ Erreur lors du traitement FFmpeg")
            with st.expander("Voir les détails de l'erreur"):
                st.code(e.stderr)

        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"❌ Erreur inattendue: {str(e)}")

elif uploaded_video and not uploaded_mask:
    st.warning("⚠️ Veuillez également charger un masque PNG pour continuer.")
elif uploaded_mask and not uploaded_video:
    st.warning("⚠️ Veuillez également charger une vidéo pour continuer.")
else:
    st.info("👆 Commencez par charger une vidéo et un masque PNG ci-dessus.")

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🎭 Video Masker pour projections en alcôve | Propulsé par FFmpeg et Streamlit</p>
</div>
""", unsafe_allow_html=True)
