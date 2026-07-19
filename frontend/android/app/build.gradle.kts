plugins {
    id("com.android.application")
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "com.trmex.personal_ai_assistant"
    compileSdk = 36
    ndkVersion = flutter.ndkVersion

    signingConfigs {
        create("release") {
            storeFile = file("/home/runner/work/Trmex-1/Trmex-1/frontend/android/app/upload-keystore.jks")
            storePassword = System.getenv("KEYSTORE_PASSWORD")
            keyAlias = "key0"
            keyPassword = System.getenv("KEY_PASSWORD")
        }
    }

    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
            isMinifyEnabled = true
        }
    }
}

flutter {
    source = "../.."
}
