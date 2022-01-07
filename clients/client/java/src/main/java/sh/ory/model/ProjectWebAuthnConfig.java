/*
 * Ory APIs
 * Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 
 *
 * The version of the OpenAPI document: v0.0.1-alpha.42
 * Contact: support@ory.sh
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package sh.ory.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.net.URI;

/**
 * ProjectWebAuthnConfig
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2022-01-07T20:26:34.917598036Z[Etc/UTC]")
public class ProjectWebAuthnConfig {
  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public static final String SERIALIZED_NAME_RP_DISPLAY_NAME = "rp_display_name";
  @SerializedName(SERIALIZED_NAME_RP_DISPLAY_NAME)
  private String rpDisplayName;

  public static final String SERIALIZED_NAME_RP_ICON = "rp_icon";
  @SerializedName(SERIALIZED_NAME_RP_ICON)
  private URI rpIcon;

  public static final String SERIALIZED_NAME_RP_ID = "rp_id";
  @SerializedName(SERIALIZED_NAME_RP_ID)
  private String rpId;

  public static final String SERIALIZED_NAME_RP_ORIGIN = "rp_origin";
  @SerializedName(SERIALIZED_NAME_RP_ORIGIN)
  private URI rpOrigin;


  public ProjectWebAuthnConfig enabled(Boolean enabled) {
    
    this.enabled = enabled;
    return this;
  }

   /**
   * Set to true to enable the WebAuthn authentication method.
   * @return enabled
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "Set to true to enable the WebAuthn authentication method.")

  public Boolean getEnabled() {
    return enabled;
  }


  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public ProjectWebAuthnConfig rpDisplayName(String rpDisplayName) {
    
    this.rpDisplayName = rpDisplayName;
    return this;
  }

   /**
   * The display name to show in the authenticator.
   * @return rpDisplayName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "Ory Corp", value = "The display name to show in the authenticator.")

  public String getRpDisplayName() {
    return rpDisplayName;
  }


  public void setRpDisplayName(String rpDisplayName) {
    this.rpDisplayName = rpDisplayName;
  }


  public ProjectWebAuthnConfig rpIcon(URI rpIcon) {
    
    this.rpIcon = rpIcon;
    return this;
  }

   /**
   * A URL to an icon which might be shown in the authenticator.
   * @return rpIcon
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "https://example.org/icon.png", value = "A URL to an icon which might be shown in the authenticator.")

  public URI getRpIcon() {
    return rpIcon;
  }


  public void setRpIcon(URI rpIcon) {
    this.rpIcon = rpIcon;
  }


  public ProjectWebAuthnConfig rpId(String rpId) {
    
    this.rpId = rpId;
    return this;
  }

   /**
   * This must be the hostname of the login page.
   * @return rpId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "example.org", value = "This must be the hostname of the login page.")

  public String getRpId() {
    return rpId;
  }


  public void setRpId(String rpId) {
    this.rpId = rpId;
  }


  public ProjectWebAuthnConfig rpOrigin(URI rpOrigin) {
    
    this.rpOrigin = rpOrigin;
    return this;
  }

   /**
   * This must be the scheme://hostname of the login page.
   * @return rpOrigin
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "https://example.org/", value = "This must be the scheme://hostname of the login page.")

  public URI getRpOrigin() {
    return rpOrigin;
  }


  public void setRpOrigin(URI rpOrigin) {
    this.rpOrigin = rpOrigin;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectWebAuthnConfig projectWebAuthnConfig = (ProjectWebAuthnConfig) o;
    return Objects.equals(this.enabled, projectWebAuthnConfig.enabled) &&
        Objects.equals(this.rpDisplayName, projectWebAuthnConfig.rpDisplayName) &&
        Objects.equals(this.rpIcon, projectWebAuthnConfig.rpIcon) &&
        Objects.equals(this.rpId, projectWebAuthnConfig.rpId) &&
        Objects.equals(this.rpOrigin, projectWebAuthnConfig.rpOrigin);
  }

  @Override
  public int hashCode() {
    return Objects.hash(enabled, rpDisplayName, rpIcon, rpId, rpOrigin);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectWebAuthnConfig {\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    rpDisplayName: ").append(toIndentedString(rpDisplayName)).append("\n");
    sb.append("    rpIcon: ").append(toIndentedString(rpIcon)).append("\n");
    sb.append("    rpId: ").append(toIndentedString(rpId)).append("\n");
    sb.append("    rpOrigin: ").append(toIndentedString(rpOrigin)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

